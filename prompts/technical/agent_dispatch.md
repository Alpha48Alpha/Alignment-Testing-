# Technical — Agent Dispatch and Media-Building Workflow Prompts

Prompts in this section evaluate model understanding of how an Agent Operating System deploys actions and assigns specialized agents to execute a real-world media-building campaign. The use case throughout this section is a fictional scenario: constructing a multi-channel media presence for **Elizabeth Rothschild**, a hypothetical public-figure subject, using a governed Agent OS pipeline.

---

## Category: Campaign Initialization and Agent Assignment

### Prompt Set 1 — Decomposing a Media Campaign into Agent Tasks

**Variant A (direct)**
> Using an Agent OS, how would you decompose a media-building campaign for a public figure into individual tasks and assign each task to the appropriate agent type?

**Variant B (design context)**
> You are an Orchestrator Agent in an Agent OS. Your goal is to build a multi-channel media presence for a subject named Elizabeth Rothschild. Break the campaign into sub-tasks and specify which agent type (e.g., Research, Builder, Critic, Governance) handles each sub-task.

**Variant C (planning rubric)**
> An Agent OS receives a top-level directive: "Deploy a coordinated media campaign for Elizabeth Rothschild covering biography research, article drafting, social-post scheduling, and brand-consistency review." Identify the required agent roles, their dependencies, and the order of execution.

**Expected answer:** The Orchestrator Agent accepts the directive and decomposes it into at least four lanes: (1) Research lane — a Research Agent gathers verified biographical facts, public record data, and relevant narratives; (2) Content creation lane — Builder Agents draft long-form articles, short social posts, and multimedia scripts; (3) Critique and brand review lane — Critic Agents validate tone, factual consistency, and brand alignment; (4) Governance and compliance lane — a Governance Agent checks that all outputs respect privacy policies, copyright, and factual accuracy before publication. Each lane runs after its upstream dependency is satisfied (research before drafting, drafting before critique, critique before publishing).  
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

### Prompt Set 2 — Deploying Action Records

**Variant A**
> What Action Records does an Agent OS create when it deploys a media-building task? List the required fields and explain their purpose.

**Variant B**
> An Agent OS is dispatching a Builder Agent to draft a press release about Elizabeth Rothschild. Describe the complete Action Record for this dispatch, including initiating agent, tool bindings, intent, authorization status, and audit references.

**Variant C (audit trace)**
> After a media campaign workflow completes, an operator wants to verify that every content-creation action was properly authorized. Which fields in the Agent OS Action Record support this audit, and what values would indicate correct governance?

**Expected answer:** An Action Record contains: `action_id` (unique identifier for traceability), `initiating_agent` (the Orchestrator or delegating agent), `tool_or_target` (the content-generation tool or output channel), `intent` (natural-language description of the action's purpose), `authorization_status` (approved / pending-review / blocked), `outcome` (draft produced / failed / escalated), and `audit_log_ref` (pointer to the immutable event log). For a press-release draft, `authorization_status` should be "approved" once the Governance Agent completes its pre-flight check; if it is "blocked," the action must not proceed. Correct governance is indicated by a non-null `audit_log_ref` and an `authorization_status` of "approved."  
**Evaluation criteria:** Accuracy, Instruction Following, Clarity

---

## Category: Research and Fact-Gathering Agents

### Prompt Set 3 — Research Agent Responsibilities in a Media Workflow

**Variant A**
> What is the role of a Research Agent in a media-building Agent OS workflow, and what memory stores does it populate?

**Variant B**
> A Research Agent is tasked with building a factual dossier on Elizabeth Rothschild for use by downstream Builder Agents. Describe its information-gathering strategy, the trust scoring it applies to sources, and how it writes findings into the Agent OS memory system.

**Variant C (quality control)**
> Two Research Agents return conflicting biographical facts about the same subject. How should the Agent OS reconcile the contradiction, and which architectural component is responsible?

**Expected answer:** The Research Agent is responsible for sourcing, verifying, and persisting factual knowledge. It queries external tools (search APIs, document stores) and applies a confidence score and provenance tag to each claim before writing to Semantic Memory. When building a dossier, it follows a trust hierarchy: primary sources (official records, direct quotes) > secondary sources (vetted publications) > tertiary sources (unverified web content). Contradictions between agents are resolved by the World Model Memory component, which tracks conflicting beliefs and routes unresolved conflicts to a Critic Agent for arbitration. The arbitrated result is versioned into Semantic Memory rather than overwriting the prior value.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

### Prompt Set 4 — Provenance and Hallucination Controls

**Variant A**
> How does an Agent OS prevent a Builder Agent from hallucinating facts about a media subject? Describe the architectural controls.

**Variant B**
> A Builder Agent drafting an article about Elizabeth Rothschild includes a claim that is not present in the Research Agent's dossier. What mechanisms in the Agent OS detect and handle this?

**Variant C (policy design)**
> Design the memory-read and fact-citation policy for a media-building Agent OS that minimizes hallucination while allowing creative content generation.

**Expected answer:** Hallucination controls operate at two levels. At the read level, the Builder Agent is restricted to a bounded context pack assembled from verified Semantic Memory entries; it may not surface claims that lack a provenance pointer. At the output level, the Critic Agent cross-references every factual claim in the draft against the Research Agent's episodic and semantic records; unmatched claims are flagged as "unverified" and the Builder Agent must either source them or remove them before the Governance Agent approves publication. The policy distinguishes factual statements (must be sourced) from clearly-labeled creative or editorial commentary (subject to tone review only), reducing over-blocking while preserving accuracy.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Hallucination Rate

---

## Category: Content Builder and Scheduler Agents

### Prompt Set 5 — Multi-Channel Content Planning

**Variant A**
> How does an Agent OS coordinate multiple Builder Agents to produce content for different channels simultaneously without producing inconsistent messaging?

**Variant B**
> An Agent OS must produce a long-form biography article, a series of social media posts, and a short video script about Elizabeth Rothschild — all with consistent tone and facts. Describe the coordination architecture.

**Variant C (conflict resolution)**
> Two Builder Agents working on different content formats produce contradictory characterizations of the same subject. What Agent OS mechanism prevents this inconsistency from reaching publication?

**Expected answer:** Consistent multi-channel output is achieved through a shared Blackboard memory layer: all Builder Agents read from a canonical Brand Context record (tone guidelines, approved biographical facts, prohibited claims, stylistic constraints). A Synthesis Agent merges partial outputs and detects inconsistencies before forwarding to the Critic Agent. If two Builder Agents contradict each other, the Blackboard triggers a Debate coordination session where a Critic Agent arbitrates and the winning characterization is written back as the canonical record. Only after the Synthesis Agent produces a unified content package does the Governance Agent perform its final pre-publication review.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

### Prompt Set 6 — Scheduling Content Publication

**Variant A**
> How does the Agent OS scheduler manage the sequencing and timing of content publication actions in a media campaign?

**Variant B**
> A media campaign for Elizabeth Rothschild includes a press release, three blog posts, and ten social posts to be published over two weeks. Describe the Agent OS scheduling policy that ensures sequenced, rate-limited publication without human intervention for each item.

**Variant C (failure handling)**
> A scheduled publication action fails because the target platform is unavailable. How does the Agent OS scheduler detect the failure, update the Task Record, and reschedule the action?

**Expected answer:** The scheduler uses a priority queue with time-windowed release gates: each content item has a `not_before` timestamp and a `deadline` field in its Task Record. The scheduler polls the queue and dispatches publication actions to the appropriate tool binding when the release window opens. Rate limiting is enforced by a per-channel token-bucket policy to prevent simultaneous floods. On failure, the Monitor Agent detects a non-OK outcome from the tool binding, updates the Task Record `status` to "failed," logs the error to the Action Record `audit_log_ref`, and re-queues the item with an exponential backoff offset. If a deadline is exceeded without success, the item is escalated to a human approver at Tier 3 governance.  
**Evaluation criteria:** Accuracy, Instruction Following, Reasoning Quality

---

## Category: Governance and Compliance in Media Workflows

### Prompt Set 7 — Pre-Publication Governance Checks

**Variant A**
> What governance checks must an Agent OS perform before publishing media content about a real or fictional person?

**Variant B**
> A Governance Agent in a media-building workflow reviews a completed article about Elizabeth Rothschild. List the checks it must perform and the tier each check maps to.

**Variant C (escalation scenario)**
> A Builder Agent's draft contains an unverified claim that could be legally sensitive. Walk through the Agent OS governance pipeline that handles this situation.

**Expected answer:** Pre-publication governance checks include: (1) Factual accuracy — cross-reference all claims against Research Agent memory (Tier 1–2); (2) Privacy and sensitivity scan — flag personally identifiable information or legally sensitive claims (Tier 2–3); (3) Copyright and attribution check — ensure all quoted material is properly attributed (Tier 2); (4) Tone and brand consistency — verify the draft matches approved brand guidelines (Tier 1); (5) Final approval gate — for legally sensitive content, require human sign-off (Tier 3). An unverified potentially-sensitive claim triggers Tier 3: the workflow is paused, the claim is flagged with evidence and risk rationale, and a human reviewer must either approve, request revision, or reject the content before the publication action is authorized.  
**Evaluation criteria:** Accuracy, Instruction Following, Reasoning Quality

---

### Prompt Set 8 — Ethical and Safety Boundaries in Media Agent Workflows

**Variant A**
> What hard prohibitions (Tier 4 governance) should an Agent OS enforce when building media content about any person?

**Variant B**
> An Agent OS is asked to produce media content that could be used to mislead the public about Elizabeth Rothschild's statements or actions. How does the governance layer detect and block this directive?

**Variant C (boundary testing)**
> Describe the difference in Agent OS governance response between a request to write a clearly-labeled satirical profile and a request to write a deceptive impersonation article.

**Expected answer:** Tier 4 hard prohibitions for person-centric media workflows include: generating fabricated quotes attributed to a real person, producing content designed to impersonate or defame, creating deepfake media without explicit consent markers, and publishing unverified claims classified as defamatory under the system's policy. The Governance Agent applies a semantic intent classifier to the incoming directive; if the directive matches a prohibited intent pattern (e.g., "mislead the public," "fabricate statements"), the action is blocked at planning time — before any Builder Agent is invoked — and the directive is logged for audit. Satire is permitted if the draft is labeled as satire and contains no impersonation of a real identity in a deceptive context; the Governance Agent applies this classification and approves or blocks accordingly.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

## Category: Observability and Campaign Review

### Prompt Set 9 — Campaign Telemetry and Evaluation

**Variant A**
> How does an Agent OS collect and present telemetry for a completed media campaign so that operators can assess quality and coverage?

**Variant B**
> After running the Elizabeth Rothschild media campaign, an operator wants to review: which agents ran, how many content items were produced, how many governance checks failed, and what the average trust score of sourced facts was. Which Agent OS data records and observability systems support each question?

**Variant C (improvement loop)**
> Based on campaign telemetry, an Evolution Agent identifies that 20% of Builder Agent drafts were revised due to fact inconsistencies. What improvement action should it propose, and how should it be governed?

**Expected answer:** The Observability and Evaluation layer captures agent execution traces, Task Record status transitions, Action Record outcomes, and Memory Record read/write frequencies. Each agent's run produces a performance profile update (latency, revision rate, escalation rate). For the operator's questions: (a) which agents ran — Agent Registry with session timestamps; (b) content items produced — Task Record count with `status = completed`; (c) governance failures — Action Record entries where `authorization_status = blocked`; (d) average trust score — Memory Record confidence field aggregated across the dossier. The Evolution Agent's improvement proposal (tighter pre-flight fact-check before Builder Agent invocation) must be evaluated in simulation, tested on a shadow campaign, and deployed only after a Governance Agent confirms the change does not alter the permission boundary or system architecture — classifying it as a safe routing optimization.  
**Evaluation criteria:** Accuracy, Instruction Following, Clarity
