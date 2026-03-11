"""
prompt_tester.py

Run a set of prompts against an OpenAI-compatible API and save responses to a
JSON file for later scoring.

Usage:
    python prompt_tester.py --input prompts.json --output responses.json --model gpt-4o

Input format (prompts.json):
    [
        {
            "id": "PS1-A",
            "domain": "technical",
            "metric": "reasoning_quality",
            "prompt": "What is the time complexity of binary search?"
        },
        ...
    ]

Output format (responses.json):
    [
        {
            "id": "PS1-A",
            "domain": "technical",
            "metric": "reasoning_quality",
            "prompt": "What is the time complexity of binary search?",
            "response": "O(log n)...",
            "model": "gpt-4o",
            "temperature": 0
        },
        ...
    ]
"""

import argparse
import json
import os
import sys
import time

try:
    from openai import OpenAI
except ImportError:
    sys.exit("openai package not found. Install with: pip install openai")


def load_prompts(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        sys.exit(f"Expected a JSON array in {path}, got {type(data).__name__}")
    return data


def run_prompt(client: "OpenAI", prompt: str, model: str, temperature: float) -> str:
    """Send a single prompt to the model and return the response text.

    Args:
        client: Initialized OpenAI client.
        prompt: The user message to send.
        model: Model identifier (e.g. "gpt-4o").
        temperature: Sampling temperature; 0 for deterministic output.

    Returns:
        The model's response as a string.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content or ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Run prompts against an OpenAI model")
    parser.add_argument("--input", required=True, help="Path to prompts JSON file")
    parser.add_argument("--output", required=True, help="Path to write responses JSON file")
    parser.add_argument("--model", default="gpt-4o", help="Model name (default: gpt-4o)")
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature (default: 0 for deterministic output)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls (default: 0.5)",
    )
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OPENAI_API_KEY environment variable not set")

    client = OpenAI(api_key=api_key)
    prompts = load_prompts(args.input)

    results = []
    for i, item in enumerate(prompts, start=1):
        prompt_text = item.get("prompt", "")
        if not prompt_text:
            print(f"[{i}/{len(prompts)}] Skipping item with missing 'prompt' field: {item.get('id', '?')}")
            continue

        print(f"[{i}/{len(prompts)}] Running prompt {item.get('id', '?')}...")
        response_text = run_prompt(client, prompt_text, args.model, args.temperature)

        result = {
            **item,
            "response": response_text,
            "model": args.model,
            "temperature": args.temperature,
        }
        results.append(result)

        if args.delay > 0 and i < len(prompts):
            time.sleep(args.delay)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {len(results)} responses written to {args.output}")


if __name__ == "__main__":
    main()
