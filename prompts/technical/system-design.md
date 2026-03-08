# Technical Prompts — System Design
**Domain:** Technical | **Subdomain:** System Design  
**Total Prompts:** 35  
**Evaluation Criteria:** scalability reasoning, trade-off analysis, architectural clarity, completeness

---

## Fundamentals

**SD-001**  
`Design a URL shortener (like bit.ly). Cover: API design, data storage, hash generation, collision handling, redirect performance, and analytics. Estimate QPS and storage.`  
*Tags: system design, URL shortener, classic, intermediate*

**SD-002**  
`Design a rate limiter that can be applied per-user and per-IP. Explain the token bucket and sliding window algorithms. Compare their accuracy and memory usage.`  
*Tags: rate limiting, algorithms, distributed systems, intermediate*

**SD-003**  
`Explain the CAP theorem with concrete examples for each tradeoff pair (CP, AP, CA). Which common databases fall into each category?`  
*Tags: CAP theorem, distributed systems, databases, intermediate*

**SD-004**  
`What is consistent hashing? Explain with a diagram how it distributes load and handles node additions/removals with minimal data redistribution.`  
*Tags: consistent hashing, load balancing, distributed systems, advanced*

**SD-005**  
`Compare SQL and NoSQL databases across: ACID properties, scalability, schema flexibility, and query patterns. Give 3 examples of when to choose each.`  
*Tags: SQL vs NoSQL, database selection, intermediate*

---

## Scalability & Performance

**SD-006**  
`Design a caching strategy for a high-traffic e-commerce product catalog. Discuss cache invalidation, TTL, eviction policies, and where to place caches (CDN, in-memory, DB query cache).`  
*Tags: caching, CDN, Redis, e-commerce, intermediate*

**SD-007**  
`Explain horizontal vs vertical scaling. Design a horizontally scalable web application architecture. What components become bottlenecks and how do you address them?`  
*Tags: scaling, architecture, intermediate*

**SD-008**  
`Design a read-heavy system using database replication. Explain primary-replica replication, replication lag, and how to handle stale reads.`  
*Tags: database replication, read scaling, advanced*

**SD-009**  
`What is database sharding? Describe range-based, hash-based, and directory-based sharding. What are the operational challenges of each?`  
*Tags: sharding, database partitioning, advanced*

**SD-010**  
`Design a global content delivery network (CDN). How does anycast routing work? How do you handle cache misses and origin fallback at the edge?`  
*Tags: CDN, anycast, edge computing, advanced*

---

## Microservices & APIs

**SD-011**  
`Design a microservices architecture for an online food delivery app. Identify the key services, define their responsibilities, and draw the communication flow.`  
*Tags: microservices, architecture, intermediate*

**SD-012**  
`Explain service discovery in a microservices ecosystem. Compare client-side discovery (Eureka) with server-side discovery (AWS ALB). When would you use each?`  
*Tags: service discovery, microservices, intermediate*

**SD-013**  
`Design a REST API for a banking application. Define resource naming conventions, HTTP verbs, status codes, versioning strategy, and authentication flow.`  
*Tags: REST API, API design, banking, intermediate*

**SD-014**  
`Compare REST, GraphQL, and gRPC. For each: describe its ideal use case, performance characteristics, and a scenario where it would be the wrong choice.`  
*Tags: API protocols, comparison, intermediate*

**SD-015**  
`Implement the Saga pattern for a distributed transaction (e.g., booking a flight + hotel + car). Explain choreography vs. orchestration sagas.`  
*Tags: distributed transactions, Saga pattern, advanced*

---

## Messaging & Event-Driven Architecture

**SD-016**  
`Design an event-driven notification system using a message queue (Kafka or RabbitMQ). Explain the producer-consumer model, message durability, and at-least-once delivery.`  
*Tags: event-driven, Kafka, messaging, intermediate*

**SD-017**  
`Explain the difference between message queues and event streams. When would you use Kafka vs SQS vs RabbitMQ? Discuss ordering, retention, and scalability.`  
*Tags: messaging systems, Kafka, SQS, comparison, advanced*

**SD-018**  
`Design a real-time collaborative document editing system (like Google Docs). How do you handle concurrent edits using Operational Transformation or CRDTs?`  
*Tags: real-time, CRDTs, collaboration, advanced*

**SD-019**  
`Build a pub/sub notification architecture for a social media feed. How do you handle fan-out for users with millions of followers efficiently?`  
*Tags: fan-out, pub/sub, social media, advanced*

---

## Storage & Data Systems

**SD-020**  
`Design a distributed object storage system (like S3). Cover: object addressing, data durability (replication vs erasure coding), consistency, and large file uploads.`  
*Tags: object storage, distributed systems, advanced*

**SD-021**  
`Design a time-series database for IoT sensor data. What data model, compression strategies, and query optimizations would you apply?`  
*Tags: time-series, IoT, database design, advanced*

**SD-022**  
`Explain write-ahead logging (WAL) in databases. How does it ensure durability and enable point-in-time recovery? Give examples from PostgreSQL.`  
*Tags: WAL, database internals, durability, advanced*

**SD-023**  
`Design a search engine index for a document corpus. Explain the inverted index structure, tokenization, and ranking using TF-IDF.`  
*Tags: search engine, inverted index, information retrieval, advanced*

---

## Reliability & Observability

**SD-024**  
`Define SLA, SLO, and SLI. Create a realistic set of SLOs for an e-commerce checkout API. What error budget would you set and how would you track it?`  
*Tags: SRE, SLA/SLO/SLI, reliability, intermediate*

**SD-025**  
`Design a distributed tracing system for a microservices application. How does OpenTelemetry work, and how do you correlate spans across services?`  
*Tags: observability, distributed tracing, OpenTelemetry, advanced*

**SD-026**  
`Explain the circuit breaker pattern. How does it improve system resilience? Implement a conceptual circuit breaker with three states: Closed, Open, Half-Open.`  
*Tags: circuit breaker, resilience, design patterns, intermediate*

**SD-027**  
`Design a disaster recovery (DR) strategy for a critical web application. Define RTO and RPO. Compare multi-region active-active vs active-passive approaches.`  
*Tags: disaster recovery, RTO/RPO, high availability, advanced*

---

## Security Architecture

**SD-028**  
`Design an authentication and authorization system using OAuth 2.0 and JWT. Explain the authorization code flow, token lifecycle, and refresh token security.`  
*Tags: OAuth 2.0, JWT, authentication, intermediate*

**SD-029**  
`Design a zero-trust network architecture for an enterprise application. What does "never trust, always verify" mean in practice at each layer?`  
*Tags: zero-trust, security architecture, advanced*

**SD-030**  
`Explain end-to-end encryption for a messaging app. How does the Signal Protocol's Double Ratchet algorithm provide forward secrecy?`  
*Tags: encryption, Signal Protocol, messaging security, advanced*

---

## Infrastructure & Cloud

**SD-031**  
`Design a Kubernetes-based deployment for a multi-tier web application. Include Deployments, Services, Ingress, ConfigMaps, Secrets, and HPA.`  
*Tags: Kubernetes, infrastructure, cloud-native, advanced*

**SD-032**  
`Compare serverless (AWS Lambda), containers (ECS/EKS), and VMs (EC2) for deploying a microservice. Discuss cold start, cost, scalability, and operational overhead.`  
*Tags: cloud architecture, serverless, containers, intermediate*

**SD-033**  
`Design an infrastructure-as-code (IaC) workflow for a multi-environment cloud setup (dev/staging/prod) using Terraform. Explain state management and drift detection.`  
*Tags: IaC, Terraform, DevOps, advanced*

**SD-034**  
`Design a multi-region active-active deployment for a global SaaS application. Address data synchronization, latency-based routing, and conflict resolution.`  
*Tags: multi-region, global scale, advanced*

**SD-035**  
`Estimate the infrastructure cost for a social media app serving 1 million daily active users. Break down compute, storage, bandwidth, and CDN costs. State your assumptions.`  
*Tags: cost estimation, back-of-envelope, intermediate*
