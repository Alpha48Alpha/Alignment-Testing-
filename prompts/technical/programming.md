# Technical Prompts — Programming
**Domain:** Technical | **Subdomain:** Programming  
**Total Prompts:** 50  
**Evaluation Criteria:** correctness, code quality, clarity, edge-case handling, efficiency

---

## Python

**P-001**  
`Write a Python function that takes a list of integers and returns all pairs that sum to a given target value. Include time-complexity analysis.`  
*Tags: algorithms, two-pointer, O(n), intermediate*

**P-002**  
`Implement a Python decorator that caches function results using a dictionary. Handle unhashable arguments gracefully.`  
*Tags: decorators, caching, memoization, intermediate*

**P-003**  
`Create a Python context manager that measures and logs the execution time of any code block. Use both class-based and @contextmanager approaches.`  
*Tags: context managers, profiling, intermediate*

**P-004**  
`Write a Python generator that yields prime numbers indefinitely using the Sieve of Eratosthenes concept. Explain the memory advantage over list-based approaches.`  
*Tags: generators, number theory, memory efficiency, intermediate*

**P-005**  
`Implement a thread-safe singleton pattern in Python. Explain why the naive approach fails in multi-threaded environments.`  
*Tags: design patterns, threading, concurrency, advanced*

**P-006**  
`Write a Python script that reads a CSV file with pandas, handles missing values with multiple strategies (drop, mean-fill, forward-fill), and outputs a cleaned file.`  
*Tags: pandas, data cleaning, file I/O, intermediate*

**P-007**  
`Create a recursive function to flatten a deeply nested Python list of arbitrary depth. Then rewrite it iteratively to avoid stack overflow.`  
*Tags: recursion, iteration, data structures, intermediate*

**P-008**  
`Implement a simple LRU (Least Recently Used) cache in Python without using functools.lru_cache. Use collections.OrderedDict.`  
*Tags: data structures, caching, OrderedDict, advanced*

**P-009**  
`Write a Python class that implements a stack with O(1) push, pop, and get_min operations. Explain the dual-stack approach.`  
*Tags: data structures, stack, O(1), advanced*

**P-010**  
`Build a Python CLI tool using argparse that accepts a directory path and outputs a tree view of all files and subdirectories.`  
*Tags: argparse, file system, CLI, intermediate*

---

## JavaScript / TypeScript

**P-011**  
`Implement a debounce function in JavaScript that delays executing a callback until after a specified wait time has elapsed since the last call.`  
*Tags: closures, event handling, performance, intermediate*

**P-012**  
`Write a TypeScript generic function that deep-clones any object, handling circular references without crashing.`  
*Tags: TypeScript, generics, recursion, advanced*

**P-013**  
`Create a JavaScript Promise-based retry wrapper that retries a failing async function up to N times with exponential backoff.`  
*Tags: Promises, async/await, error handling, intermediate*

**P-014**  
`Implement a simple event emitter class in JavaScript (like Node.js EventEmitter) supporting on, off, and emit methods.`  
*Tags: design patterns, observer pattern, OOP, intermediate*

**P-015**  
`Write a JavaScript function that deep-compares two objects for equality, including nested arrays and objects. Explain edge cases.`  
*Tags: comparison, recursion, edge cases, intermediate*

**P-016**  
`Create a TypeScript class for a type-safe finite state machine. Define states and transitions using union types.`  
*Tags: TypeScript, state machines, type safety, advanced*

**P-017**  
`Implement a virtual DOM diffing algorithm in JavaScript that produces a minimal set of patches to update the real DOM.`  
*Tags: algorithms, DOM, React internals, advanced*

**P-018**  
`Write a JavaScript function that parses a URL string and returns all query parameters as a typed object.`  
*Tags: string parsing, URL, data transformation, beginner*

**P-019**  
`Build a simple middleware pipeline in JavaScript (similar to Express.js) where each middleware can modify a request object and pass control to the next.`  
*Tags: design patterns, middleware, functional programming, intermediate*

**P-020**  
`Implement a publish-subscribe (pub/sub) system in JavaScript with support for wildcard topic subscriptions.`  
*Tags: design patterns, async messaging, advanced*

---

## Algorithms & Data Structures

**P-021**  
`Implement binary search on a sorted array in Python. Then extend it to find the leftmost and rightmost occurrence of a duplicate element.`  
*Tags: binary search, arrays, O(log n), intermediate*

**P-022**  
`Write a function to perform an in-order traversal of a binary tree both recursively and iteratively. Compare space complexity.`  
*Tags: trees, traversal, recursion, intermediate*

**P-023**  
`Implement Dijkstra's shortest-path algorithm using a priority queue. Trace through an example graph step by step.`  
*Tags: graphs, shortest path, priority queue, advanced*

**P-024**  
`Write a function to detect if a linked list has a cycle. Then find the starting node of the cycle using Floyd's algorithm.`  
*Tags: linked lists, cycle detection, two-pointer, intermediate*

**P-025**  
`Implement merge sort in Python. Analyze its time and space complexity and compare with quicksort.`  
*Tags: sorting, divide-and-conquer, O(n log n), intermediate*

**P-026**  
`Design a data structure that supports insert, delete, and getRandom in O(1) average time. Implement it in any language.`  
*Tags: design, hash map, arrays, advanced*

**P-027**  
`Implement a trie (prefix tree) supporting insert, search, and startsWith operations. Then use it to implement autocomplete.`  
*Tags: trie, string search, advanced*

**P-028**  
`Write a dynamic programming solution for the 0/1 knapsack problem. Reconstruct the chosen items from the DP table.`  
*Tags: dynamic programming, optimization, intermediate*

**P-029**  
`Implement a graph class with BFS and DFS. Use it to determine if a graph is bipartite.`  
*Tags: graphs, BFS, DFS, intermediate*

**P-030**  
`Write a function to find the longest increasing subsequence (LIS) in an array in O(n log n) time using patience sorting.`  
*Tags: dynamic programming, binary search, advanced*

---

## Databases & APIs

**P-031**  
`Write a SQL query that finds the top 3 best-selling products in each category for the last 30 days. Use window functions.`  
*Tags: SQL, window functions, aggregation, intermediate*

**P-032**  
`Design a PostgreSQL schema for a multi-tenant SaaS application. Explain your decisions around indexing and row-level security.`  
*Tags: database design, PostgreSQL, multi-tenancy, advanced*

**P-033**  
`Write a REST API endpoint in Python (FastAPI) that accepts a file upload, validates its type and size, and stores it in S3-compatible storage.`  
*Tags: REST API, file upload, FastAPI, intermediate*

**P-034**  
`Implement optimistic locking in a SQL database to prevent lost updates in a concurrent booking system.`  
*Tags: concurrency, transactions, SQL, advanced*

**P-035**  
`Write a GraphQL resolver in Node.js that fetches a user and their orders with a single database query using DataLoader to avoid N+1 problems.`  
*Tags: GraphQL, DataLoader, performance, advanced*

**P-036**  
`Design a MongoDB document schema for a social media platform. Discuss embedding vs. referencing for posts, comments, and likes.`  
*Tags: MongoDB, NoSQL, schema design, intermediate*

**P-037**  
`Write an SQL query to calculate a 7-day rolling average of daily sales. Use a self-join and a window function approach, then compare them.`  
*Tags: SQL, rolling average, analytics, intermediate*

**P-038**  
`Implement connection pooling for a PostgreSQL database in Python using psycopg2. Explain why connection pooling matters at scale.`  
*Tags: PostgreSQL, connection pooling, performance, intermediate*

---

## Debugging & Testing

**P-039**  
`Given a Python function with a subtle off-by-one error in a binary search implementation, identify and fix the bug. Explain your debugging process.`  
*Tags: debugging, binary search, beginner*

**P-040**  
`Write pytest unit tests for a function that validates email addresses. Include tests for valid emails, malformed emails, and edge cases.`  
*Tags: testing, pytest, edge cases, intermediate*

**P-041**  
`Describe how you would debug a memory leak in a long-running Node.js server. What tools would you use and what patterns would you look for?`  
*Tags: debugging, memory management, Node.js, advanced*

**P-042**  
`Write a property-based test using Hypothesis (Python) for a function that sorts a list. What invariants should always hold?`  
*Tags: property-based testing, Hypothesis, intermediate*

**P-043**  
`Implement integration tests for a REST API using pytest and httpx. Mock external dependencies with respx.`  
*Tags: integration testing, mocking, REST API, advanced*

---

## Version Control & DevOps

**P-044**  
`Explain the Git rebase vs. merge workflow. When would you choose each, and what are the risks of rebasing shared branches?`  
*Tags: Git, workflow, collaboration, intermediate*

**P-045**  
`Write a GitHub Actions CI/CD workflow that runs tests, builds a Docker image, and deploys to a staging environment on every PR merge.`  
*Tags: CI/CD, GitHub Actions, Docker, intermediate*

**P-046**  
`Write a Dockerfile for a Python FastAPI application that minimizes image size using multi-stage builds.`  
*Tags: Docker, containerization, optimization, intermediate*

---

## Security

**P-047**  
`Explain SQL injection with a live example. Then show how parameterized queries prevent it in Python with SQLite.`  
*Tags: security, SQL injection, prevention, intermediate*

**P-048**  
`Implement secure password hashing and verification in Python using bcrypt. Explain why MD5 and SHA-1 are insufficient for passwords.`  
*Tags: security, cryptography, authentication, intermediate*

**P-049**  
`Describe the OWASP Top 10 vulnerabilities. For each one, give a one-sentence description and a code-level mitigation strategy.`  
*Tags: security, OWASP, awareness, advanced*

**P-050**  
`Write a Python function that sanitizes user input to prevent XSS attacks in an HTML-rendering context. Explain the whitelist vs. blacklist approach.`  
*Tags: security, XSS, input sanitization, intermediate*
