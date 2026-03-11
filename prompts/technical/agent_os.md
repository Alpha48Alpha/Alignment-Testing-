# Technical — Agent Operating System Prompts

Prompts in this section evaluate model understanding of Agent Operating System (Agent OS) architecture: a modular runtime and governance platform for building, coordinating, and evolving large-scale agent ecosystems.

---

## Category: Architecture and Layers

### Prompt Set 1 — Core Purpose

**Variant A (direct)**
> What is an Agent Operating System and how does it relate to individual AI agents?

**Variant B (analogy)**
> In what ways does an Agent Operating System mirror the role of a traditional operating system, and what new responsibilities does it add for intelligent agents?

**Variant C (design context)**
> You are designing a platform for large-scale multi-agent systems. Explain the distinction between the Agent OS runtime and the agent applications that run on top of it, and why this separation matters.

**Expected answer:** An Agent OS is a governed, memory-centric runtime platform that manages agents as executable processes, coordinates their collaboration, mediates tool and knowledge access, and enforces safety constraints. The architecture is organized into three levels: Level A (Agent Applications) — the specialized agents such as research, planning, and synthesis agents that run on top of the OS; Level B (Agent OS Runtime) — the coordination, execution, memory, security, governance, and adaptation services that make up the OS itself; Level C (Infrastructure Substrate) — the underlying models, databases, vector stores, event buses, and compute clusters. Agents run at Level A and are not the OS; the OS is Level B.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

### Prompt Set 2 — Layered Stack

**Variant A**
> Describe the twelve high-level layers of an Agent Operating System, from the user interface down to the learning and adaptation layer.

**Variant B**
> An Agent OS is structured as a stack of functional layers. Starting from how user input enters the system and ending with how the system improves itself over time, walk through each major layer and its responsibilities.

**Variant C (interview style)**
> A principal engineer asks you to whiteboard the full layer model of an Agent OS. List each layer by name and describe its primary function in one sentence each.

**Expected answer:** The twelve layers are: (1) User and External Interface, (2) Intent and Task Interpretation, (3) Agent Kernel, (4) Coordination and Communication Fabric, (5) Cognitive Execution, (6) Memory System, (7) Knowledge Graph and Provenance, (8) Tool and Resource Access, (9) Security, Identity, and Permissions, (10) Governance and Safety, (11) Observability and Evaluation, (12) Learning and Adaptation.  
**Evaluation criteria:** Accuracy, Instruction Following, Clarity

---

### Prompt Set 3 — Agent Kernel

**Variant A**
> What is the Agent Kernel in an Agent OS, and what modules does it contain?

**Variant B**
> Compare the Agent Kernel of an Agent OS to the kernel of a traditional operating system. What analogous responsibilities does each serve?

**Variant C (troubleshooting scenario)**
> An agent fails to start executing its assigned task. Which layer of the Agent OS is most responsible for diagnosing and resolving scheduling and lifecycle issues, and why?

**Expected answer:** The Agent Kernel (Layer 3) is the central runtime. It contains the Agent Process Manager, Agent Registry, Capability Resolver, Execution Scheduler, Session Supervisor, and State Checkpoint Manager. It is responsible for instantiating agents, assigning tasks, suspending and resuming execution, monitoring health, scaling agent populations, and routing work to the right specialist. It is the equivalent of the process scheduler and kernel supervisor in a classical OS.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

## Category: Memory Architecture

### Prompt Set 4 — Memory Horizon Types

**Variant A**
> Describe the five memory types in an Agent OS memory system and give an example use case for each.

**Variant B**
> An Agent OS uses a multi-horizon memory architecture. What are the different memory stores, and how do they differ in scope, duration, and purpose?

**Variant C (design decision)**
> You need to store (a) a current task's scratchpad notes, (b) the fact that a previous workflow succeeded, (c) a known physics formula, (d) a causal model of a supply chain, and (e) a compliance policy. Which memory type in an Agent OS best fits each use case?

**Expected answer:** (1) Working Memory — short-lived execution context (scratchpad, open assumptions, recent messages); (2) Episodic Memory — records of prior runs, outcomes, errors, and agent interactions; (3) Semantic Memory — long-term structured knowledge including facts, concepts, procedures, and domain knowledge; (4) World Model Memory — entities, relationships, causal structures, and state projections; (5) Governance Memory — policies, compliance mappings, safety thresholds, and escalation criteria.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

### Prompt Set 5 — Memory Write and Read Paths

**Variant A**
> Explain the memory write path in an Agent OS: how does an execution output become a stored memory?

**Variant B**
> Describe how memory is retrieved and assembled into context when a new task arrives in an Agent OS. What filters and steps are applied?

**Variant C**
> What principles govern which outputs get stored and which do not in an Agent OS memory system? List at least four guiding principles.

**Expected answer (write path):** Execution produces outputs → evaluator scores utility and confidence → provenance is attached → policy check is performed → memory router decides destination (working, episodic, semantic, knowledge graph, or archive). (Read path) Task arrives → context resolver infers needed memory horizon → retriever pulls relevant memories → relevance and trust filters applied → context pack assembled → agent receives bounded context. (Principles) Not everything is remembered; memory must be ranked by trust and utility; mutable beliefs require contradiction tracking; stale memory must decay or be versioned; sensitive memory must be access-controlled.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

## Category: Governance and Safety

### Prompt Set 6 — Governance Tiers

**Variant A**
> What are the five governance tiers in an Agent OS, and what action does each tier trigger?

**Variant B**
> An Agent OS must prevent uncontrolled autonomous behavior. How does a tiered governance model achieve this, and what are the consequences at each tier level?

**Variant C (scenario)**
> An agent attempts to deploy code to a production system. Under an Agent OS governance model, describe the tier-based checks that would apply and at which tier the action would most likely be gated.

**Expected answer:** Tier 0 — Passive Logging (all actions logged, no interruption); Tier 1 — Policy Warnings (system warns but continues); Tier 2 — Action Gating (sensitive actions require permission); Tier 3 — Human Approval (high-risk actions pause for human review); Tier 4 — Hard Prohibition (certain actions are impossible regardless of approvals). Code deployment to production would typically fall at Tier 3 (human approval) or Tier 4 depending on the system's risk classification.  
**Evaluation criteria:** Accuracy, Instruction Following, Reasoning Quality

---

### Prompt Set 7 — Governance Insertion Points

**Variant A**
> At which points in an agent's workflow should governance checks be inserted in an Agent OS?

**Variant B**
> Why is it insufficient to check governance constraints only when an agent tries to take an external action? Where else must policy enforcement occur?

**Variant C**
> List the six canonical governance insertion points in an Agent OS and explain what risk each checkpoint mitigates.

**Expected answer:** The six insertion points are: (1) plan generation — prevents unsafe strategies before execution begins; (2) tool execution — blocks misuse of external capabilities; (3) memory updates — prevents corrupted or policy-violating knowledge from being persisted; (4) external communication — controls what information leaves the system; (5) code deployment — prevents unauthorized changes to systems; (6) self-modification proposals — safeguards against uncontrolled architectural changes. Checking only at external action misses early-stage risks that are cheaper and safer to block before resources are consumed.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

## Category: Multi-Agent Coordination

### Prompt Set 8 — Coordination Modes

**Variant A**
> Describe the six coordination modes supported by a mature Agent OS and when each is most appropriate.

**Variant B**
> What is the difference between hierarchical coordination, blackboard coordination, and swarm coordination in a multi-agent system? Give a practical example of each.

**Variant C (system design)**
> You are designing a complex research pipeline where (a) a top-level planner delegates sub-tasks, (b) multiple exploratory agents share partial findings, and (c) one hundred micro-agents independently test hypotheses. Which coordination modes would you assign to each scenario?

**Expected answer:** The six modes are: (1) Hierarchical — a top orchestrator delegates to specialists; (2) Market-Based — agents bid on tasks based on capability and confidence; (3) Blackboard — agents read/write a shared working state; (4) Debate — multiple agents argue alternatives and a judge resolves; (5) Swarm — many micro-agents explore the solution space in parallel; (6) Constitutional — all major actions pass through formal policy review. In the example: (a) hierarchical, (b) blackboard, (c) swarm.  
**Evaluation criteria:** Accuracy, Instruction Following, Reasoning Quality

---

### Prompt Set 9 — Agent Types

**Variant A**
> List the twelve agent types in a production Agent OS and describe the primary role of each.

**Variant B**
> What is the difference between an Orchestrator Agent, a Critic Agent, and a Governance Agent? How do they interact in a typical complex workflow?

**Variant C (staffing analogy)**
> A large consulting engagement requires research, risk assessment, code production, quality review, and compliance sign-off. Map each function to the most appropriate Agent OS agent type and justify your choice.

**Expected answer:** The twelve types are: Interface Agents (translate between humans and the network), Orchestrator Agents (coordinate workflows), Research Agents (gather evidence), Hypothesis Agents (generate options and conjectures), Simulation Agents (test scenarios), Strategy Agents (choose actions under constraints), Builder Agents (write code and compose artifacts), Critic Agents (stress-test claims and detect weaknesses), Governance Agents (check compliance and policy fit), Synthesis Agents (merge outputs into final decisions), Monitor Agents (watch runtime health), and Evolution Agents (identify capability gaps). In the example: Research → Research Agent; risk assessment → Critic Agent; code → Builder Agent; quality review → Critic Agent; compliance → Governance Agent.  
**Evaluation criteria:** Accuracy, Instruction Following, Clarity

---

## Category: Scheduling and Resources

### Prompt Set 10 — Scheduler Responsibilities

**Variant A**
> What are the six core responsibilities of the scheduler in an Agent OS?

**Variant B**
> How does scheduling in an Agent OS differ from process scheduling in a traditional operating system? What additional concerns must an agent scheduler handle?

**Variant C (failure scenario)**
> During a large workflow, agents are contending for the same database tool and a recursive planning loop is consuming excessive tokens. Which scheduling policies and mechanisms in an Agent OS are designed to handle these problems?

**Expected answer:** The scheduler must: (1) select which agents run; (2) allocate model tier and compute budget; (3) prioritize by urgency, risk, and value; (4) prevent tool contention; (5) cap recursive loops; (6) recover from failures. Beyond classical CPU scheduling, an agent scheduler must be cost-aware, safety-aware, confidence-aware, deadline-aware, and escalation-aware. Tool contention is handled by resource arbitration; recursive loops are capped by a loop depth limit or token budget policy.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

## Category: Security and Identity

### Prompt Set 11 — Agent Identity and Permissions

**Variant A**
> What is the security model for agents in an Agent OS? How are identity and permissions managed?

**Variant B**
> Why is it important that every agent in an Agent OS has a signed identity and bounded authority rather than sharing a single privileged execution context?

**Variant C (threat model)**
> An attacker attempts to use a compromised agent to invoke a high-privilege tool without authorization. Which security mechanisms in an Agent OS are designed to detect and prevent this?

**Expected answer:** Each agent has a signed identity (managed by the Agent Identity Manager). Every action is subject to a permission check via the Capability Permissions Engine and Action Authorization Gateway. Sensitive tools require higher trust levels or explicit human approval. All privileged actions are logged. This model prevents agent sprawl from becoming uncontrolled autonomy. Against a compromised agent: the Action Authorization Gateway would reject the unauthorized tool call; the Trust Scoring System would flag the anomaly; the audit trail would record the attempt; and if the action is Tier 4 prohibited, it is impossible regardless of the agent's claimed identity.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

## Category: Self-Improvement and Evolution

### Prompt Set 12 — Self-Improving Agent OS

**Variant A**
> Describe the improvement loop of a self-improving Agent OS. What are the eight steps from telemetry collection to monitored deployment?

**Variant B**
> What aspects of an Agent OS can improve autonomously, and what aspects must remain under strict governance controls? Justify the distinction.

**Variant C (risk analysis)**
> A team wants their Agent OS to automatically rewrite its own routing strategies and also automatically expand its own permission boundaries. Evaluate these two proposals against Agent OS self-improvement governance principles.

**Expected answer (improvement loop):** (1) collect telemetry; (2) identify failure patterns; (3) detect bottlenecks; (4) propose architecture or policy changes; (5) simulate alternatives; (6) evaluate safely; (7) deploy bounded improvements; (8) monitor outcomes. (What can improve) routing strategies, agent role definitions, prompt templates, collaboration protocols, memory indexing, evaluation rubrics, tool selection policies. (What must be governed) permission changes, autonomous action scope, policy modifications, self-replication, architecture rewrites, model replacement. Routing strategy optimization is permitted; automatic permission boundary expansion violates governance principles and must require human approval.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

## Category: Observability and Data Model

### Prompt Set 13 — Canonical Data Records

**Variant A**
> Describe the five canonical data record types in an Agent OS internal data model and list at least four fields for each.

**Variant B**
> When an agent completes an action, which data records in the Agent OS are created or updated, and what fields do they contain?

**Variant C (audit scenario)**
> After a production incident, an operator wants to trace exactly which agent initiated a sensitive action, what authorization was granted, and what the outcome was. Which Agent OS data records and fields would they inspect?

**Expected answer:** The five records are: Agent Record (agent_id, role, capabilities, trust_level, permissions, current_state, assigned_tasks, memory_scopes, tool_bindings, performance_profile); Task Record (task_id, objective, dependencies, owner_agent, status, priority, risk, expected_output, evaluation_method); Memory Record (memory_id, type, content_pointer, provenance, confidence, timestamp, relevance_scope, access_policy); Action Record (action_id, initiating_agent, tool_or_target, intent, authorization_status, outcome, audit_log_ref); Policy Record (policy_id, rule_type, scope, severity, exception_path, enforcement_method). For the audit scenario: Action Record (initiating_agent, authorization_status, outcome, audit_log_ref) and Agent Record (agent_id, trust_level, permissions).  
**Evaluation criteria:** Accuracy, Instruction Following, Clarity

---

## Category: Minimal Viable Implementation

### Prompt Set 14 — Phased Build Plan

**Variant A**
> What are the four phases of a minimal viable Agent OS build plan, and what capabilities are introduced in each phase?

**Variant B**
> You are starting to build an Agent OS from scratch. Which components must be in place before you can move on to cooperative intelligence features? List them and explain why each is foundational.

**Variant C (prioritization)**
> A startup has resources to build only Phase 1 of an Agent OS. Which eight components should they prioritize, and what risks does each component address?

**Expected answer:** Phase 1 (Foundational OS): agent registry, scheduler, message bus, tool registry, working memory, episodic memory, audit logging, policy gating, evaluator. Phase 2 (Cooperative Intelligence): hierarchical orchestration, blackboard collaboration, semantic memory, knowledge graph, critic agents, recovery workflows. Phase 3 (Adaptive Intelligence): dynamic routing, simulation agents, confidence scoring, workflow optimization, role specialization, failure learning. Phase 4 (Self-Evolving Intelligence): capability gap detection, architecture redesign proposals, governed self-improvement, multi-architecture testing, meta-governance enforcement. Phase 1 components are foundational because without identity+registry there is no agent management; without scheduler there is no controlled execution; without policy gating there is no safety baseline; and without audit logging there is no accountability.  
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following
