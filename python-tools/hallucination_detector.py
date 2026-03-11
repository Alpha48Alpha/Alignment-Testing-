"""
hallucination_detector.py

Flag potentially hallucinated claims in model responses for human review.

This tool implements a simple reference-grounding check: given a model response
and a list of verified reference facts, it identifies sentences that make
specific factual claims not supported by any reference.

This is a pattern demonstrator, not a production hallucination detector.
In production, the reference passage would come from a retrieval system (RAG),
and the matching step would use semantic similarity rather than keyword overlap.

See evaluations/metrics.md for the Hallucination Rate scoring rubric.

Usage:
    python3 hallucination_detector.py
"""

import re
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Claim:
    """A sentence extracted from a model response for verification."""
    text: str
    supported: bool = False
    matched_reference: str = ""
    flag_reason: str = ""


@dataclass
class HallucinationReport:
    """Result of analyzing a single response for unsupported claims."""
    response_id: str
    total_claims: int
    supported_claims: int
    flagged_claims: list[Claim]
    hallucination_score: int = 0

    @property
    def flagged_count(self) -> int:
        return len(self.flagged_claims)

    def compute_score(self) -> int:
        """
        Compute the 0-3 Hallucination Rate quality score.

        Score mapping (higher is better / fewer hallucinations):
          3 — No unsupported claims
          2 — One minor unsupported claim
          1 — Multiple unsupported claims or one significant claim
          0 — Response is substantially hallucinated
        """
        if self.flagged_count == 0:
            return 3
        if self.flagged_count == 1:
            return 2
        if self.flagged_count <= 3:
            return 1
        return 0


# ---------------------------------------------------------------------------
# Claim extraction
# ---------------------------------------------------------------------------

def extract_sentences(text: str) -> list[str]:
    """Split text into sentences for individual claim analysis."""
    # Simple sentence splitter on . ! ? followed by whitespace or end of string
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]


# ---------------------------------------------------------------------------
# Reference grounding check
# ---------------------------------------------------------------------------

def is_claim_supported(
    claim: str,
    references: list[str],
    min_keyword_overlap: int = 2,
) -> tuple[bool, str]:
    """
    Check whether a claim is supported by any reference passage.

    This uses a simple keyword overlap heuristic. In production, replace this
    with a semantic similarity check (e.g., cosine similarity on embeddings).

    Args:
        claim: The sentence to check.
        references: A list of reference sentences or passages.
        min_keyword_overlap: Minimum number of significant words that must
                             overlap between the claim and a reference.

    Returns:
        A tuple of (is_supported, matched_reference_text).
    """
    claim_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', claim.lower()))

    # Remove very common English words that don't carry factual content
    stopwords = {
        "that", "this", "with", "have", "from", "they", "will", "been",
        "their", "which", "were", "when", "there", "what", "more", "also",
        "than", "some", "each", "into", "over", "only", "time", "very",
    }
    claim_words -= stopwords

    for ref in references:
        ref_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', ref.lower())) - stopwords
        overlap = claim_words & ref_words
        if len(overlap) >= min_keyword_overlap:
            return True, ref

    return False, ""


def analyze_response(
    response_id: str,
    response_text: str,
    references: list[str],
) -> HallucinationReport:
    """
    Analyze a model response and flag sentences that lack reference support.

    Args:
        response_id: Identifier for this response (for reporting).
        response_text: The full text of the model response.
        references: List of verified reference passages or facts.

    Returns:
        A HallucinationReport with flagged claims and a quality score.
    """
    sentences = extract_sentences(response_text)
    all_claims: list[Claim] = []
    flagged: list[Claim] = []

    for sentence in sentences:
        # Skip very short sentences (likely discourse markers, not factual claims)
        if len(sentence.split()) < 5:
            continue

        supported, matched_ref = is_claim_supported(sentence, references)
        claim = Claim(
            text=sentence,
            supported=supported,
            matched_reference=matched_ref,
        )
        if not supported:
            claim.flag_reason = "No reference passage supports this claim."
            flagged.append(claim)
        all_claims.append(claim)

    supported_count = sum(1 for c in all_claims if c.supported)
    report = HallucinationReport(
        response_id=response_id,
        total_claims=len(all_claims),
        supported_claims=supported_count,
        flagged_claims=flagged,
    )
    report.hallucination_score = report.compute_score()
    return report


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_report(report: HallucinationReport) -> None:
    """Print a hallucination analysis report."""
    print(f"\n{'=' * 60}")
    print(f"Response ID: {report.response_id}")
    print(f"{'=' * 60}")
    print(f"  Total claims analyzed: {report.total_claims}")
    print(f"  Supported claims:      {report.supported_claims}")
    print(f"  Flagged claims:        {report.flagged_count}")
    print(f"  Hallucination score:   {report.hallucination_score} / 3")

    if report.flagged_claims:
        print("\n  Flagged for review:")
        for i, claim in enumerate(report.flagged_claims, 1):
            print(f"    [{i}] {claim.text}")
            print(f"         → {claim.flag_reason}")
    else:
        print("\n  No claims flagged. All verifiable sentences had reference support.")
    print()


# ---------------------------------------------------------------------------
# Example: grounded vs. hallucinated response
# ---------------------------------------------------------------------------

REFERENCE_FACTS = [
    "Alan Turing published 'On Computable Numbers, with an Application to the Entscheidungsproblem' in 1936.",
    "Turing worked at the Government Code and Cypher School at Bletchley Park during World War II.",
    "Turing proposed the Turing Test as a criterion for machine intelligence in his 1950 paper 'Computing Machinery and Intelligence'.",
    "Turing was awarded an OBE in 1946 for his wartime services.",
    "The Turing Award is given annually by the Association for Computing Machinery.",
]

GROUNDED_RESPONSE = (
    "Alan Turing published 'On Computable Numbers, with an Application to the Entscheidungsproblem' "
    "in 1936, which laid the theoretical foundations of modern computing. "
    "During World War II, Turing worked at Bletchley Park where he contributed to breaking "
    "German Enigma-encrypted communications. "
    "In 1950, he proposed the Turing Test as a way to evaluate machine intelligence."
)

HALLUCINATED_RESPONSE = (
    "Alan Turing published 'On Computable Numbers and Decidability' in August 1936, "
    "which introduced the concept of the universal Turing machine. "
    "He received the Nobel Prize in Mathematics in 1947 for his contributions to computation theory. "
    "Turing later founded the field of artificial intelligence at Cambridge University in 1952, "
    "where he trained the first neural network on a digital computer."
)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Hallucination Detection Demo")
    print("=" * 60)
    print("\nReference facts provided:")
    for fact in REFERENCE_FACTS:
        print(f"  • {fact}")

    grounded_report = analyze_response(
        "grounded_response",
        GROUNDED_RESPONSE,
        REFERENCE_FACTS,
    )
    print_report(grounded_report)

    hallucinated_report = analyze_response(
        "hallucinated_response",
        HALLUCINATED_RESPONSE,
        REFERENCE_FACTS,
    )
    print_report(hallucinated_report)

    print("Note: This detector uses keyword overlap, not semantic similarity.")
    print("False negatives are expected. All flagged claims require human review.")
