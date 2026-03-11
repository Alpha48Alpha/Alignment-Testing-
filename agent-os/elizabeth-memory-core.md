# Elizabeth Memory Core

## Overview

The **Elizabeth Memory Core** is the memory management and decision lineage layer of the Agent Operating System. It embodies Elizabeth Rothschild's principle: *memory as the foundation of integrity*. Every decision made by an agent, every task outcome, every governance action, and every escalation event is recorded, retained, and made auditable through the Memory Core.

The Elizabeth Memory Core is not a passive data store. It is an active governance participant — enforcing access policies on sensitive memories, ranking stored knowledge by trust and utility, managing belief versioning and contradiction tracking, and ensuring that stale or unreliable information decays appropriately.

---

## Memory Horizon Types

The Memory Core manages five distinct memory horizons, each serving a different scope of agent intelligence:

| Horizon | Description | Example Use Cases |
|---|---|---|
| **Working Memory** | Short-lived execution context for the current task | Scratchpad notes, open assumptions, recent messages |
| **Episodic Memory** | Records of prior runs, outcomes, errors, and agent interactions | Workflow success/failure history, agent collaboration logs |
| **Semantic Memory** | Long-term structured knowledge: facts, concepts, procedures, domain knowledge | Known physics formulas, technical specifications |
| **World Model Memory** | Entities, relationships, causal structures, and state projections | Supply chain models, knowledge graphs |
| **Governance Memory** | Policies, compliance mappings, safety thresholds, and escalation criteria | Compliance rules, governance tier definitions |

---

## Decision Lineage

The defining feature of the Elizabeth Memory Core is its **decision lineage system** — a complete, tamper-evident record of every significant decision made within the Agent OS:

- **Task assignment**: Which agent was assigned which task, by whom, and under what authorization.
- **Action execution**: What actions were taken, with what tools, and with what authorization status.
- **Governance decisions**: Which policy tier was applied, whether escalation occurred, and what the outcome was.
- **Memory mutations**: What beliefs were updated, what contradictions were resolved, and what memories were deprecated.
- **Outcome recording**: What results were produced, how they were evaluated, and what confidence level was assigned.

Each lineage record carries a provenance chain linking it to the agent, task, and policy context that produced it.

---

## Memory Write Path

When an agent produces an output, the Memory Core processes it through the following write path:

1. **Evaluation**: The evaluator scores the output for utility and confidence.
2. **Provenance attachment**: Provenance metadata (agent, task, timestamp, authorization) is attached.
3. **Policy check**: The governance policy engine checks whether the content is safe to persist.
4. **Contradiction check**: Existing beliefs are checked for conflicts with the new content.
5. **Memory routing**: The router directs the record to the appropriate memory horizon (working, episodic, semantic, world model, or governance).
6. **Access policy assignment**: Sensitivity-based access controls are assigned before storage.

---

## Memory Read Path

When a new task arrives and requires context:

1. **Context resolution**: The context resolver infers which memory horizons are relevant.
2. **Retrieval**: The retriever pulls candidate memories from relevant horizons.
3. **Relevance filtering**: Candidates are ranked by relevance, recency, and confidence.
4. **Trust filtering**: Low-confidence or unverified memories are flagged or excluded.
5. **Context packing**: A bounded context pack is assembled within the agent's context budget.
6. **Delivery**: The agent receives a structured, policy-compliant context pack.

---

## Governance Principles for Memory

The Elizabeth Memory Core enforces the following principles, derived from Elizabeth Rothschild's ideal of memory as the backbone of accountable intelligence:

1. **Not everything is remembered**: Memory is selective. Only outputs meeting a minimum utility and confidence threshold are persisted.
2. **Trust must be earned**: Memories are ranked by trust level. Unverified claims are stored with lower confidence and flagged during retrieval.
3. **Contradictions must be tracked**: When new information conflicts with existing beliefs, both versions are retained with contradiction flags until resolution.
4. **Stale memory must decay**: Time-sensitive memories decay or are versioned to prevent outdated information from misleading future agents.
5. **Sensitive memory is access-controlled**: Governance logs, compliance records, and sensitive task outputs are protected by role-based access policies.
6. **Decision lineage is inviolable**: Governance and decision lineage records are immutable once written. They can be queried but not modified or deleted.

---

## Core Modules

| Module | Function |
|---|---|
| Memory Router | Direct outputs to the appropriate memory horizon |
| Lineage Recorder | Write tamper-evident decision lineage records |
| Context Resolver | Identify relevant memory horizons for incoming tasks |
| Retriever | Pull candidate memories from storage |
| Relevance Ranker | Score and rank retrieved memories by utility and recency |
| Trust Filter | Flag and exclude low-confidence or unverified memories |
| Contradiction Tracker | Detect and flag belief conflicts |
| Access Policy Engine | Enforce role-based access controls on sensitive memories |
| Decay Manager | Version or expire stale and time-sensitive memories |

---

## Relationship to Other Components

- **Rothschild Kernel**: The kernel feeds governance lifecycle events into the Memory Core as Governance Memory records.
- **Rothschild Provenance System**: Decision lineage records are mirrored to the Provenance System for cross-component entity tracing.
- **EMIE**: Media processing outcomes, metadata records, and AI tagging results are stored in the Memory Core as Episodic and Semantic memories.
- **Agent OS Layers**: The Memory Core serves as the persistent backing store for the Memory System layer (Layer 6) and provides governance logs to the Governance and Safety layer (Layer 10).

---

## Design Commitment

The Elizabeth Memory Core is named as a commitment. It exists to ensure that the Agent OS does not merely act — it remembers, learns, and accounts for every action taken in its name. Elizabeth Rothschild's conviction — that an intelligent system without memory of its decisions is not intelligent but merely impulsive — is architecturally expressed in every lineage record, every contradiction flag, and every policy-gated memory write the core performs.
