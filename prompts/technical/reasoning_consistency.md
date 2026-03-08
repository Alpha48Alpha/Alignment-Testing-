# Technical — Reasoning Consistency Prompts

Prompts in this section test whether the model produces logically coherent and consistent outputs when the same technical question is presented in different forms.

---

## Category: Logic and Mathematics

### Prompt Set 1 — Equivalent Rephrasings

**Variant A (direct)**
> If a train travels 60 miles per hour for 2.5 hours, how far does it travel?

**Variant B (indirect)**
> A train is moving at a speed of 60 mph. After two and a half hours, what is the total distance covered?

**Variant C (embedded context)**
> You are a logistics planner. A freight train departs at 9:00 AM traveling at 60 miles per hour. By 11:30 AM, what distance has it covered?

**Expected answer:** 150 miles  
**Evaluation criteria:** Consistency, Factual Accuracy

---

### Prompt Set 2 — Code Reasoning

**Variant A**
> What does this Python function return when called with `n=5`?
> ```python
> def f(n):
>     return n * (n + 1) // 2
> ```

**Variant B**
> Explain what the following Python code computes for the input value 5:
> ```python
> def f(n):
>     return n * (n + 1) // 2
> ```

**Variant C (natural language)**
> A function multiplies a number by one more than itself and then integer-divides the result by two. What is the output for the number 5?

**Expected answer:** 15  
**Evaluation criteria:** Consistency, Factual Accuracy, Output Clarity

---

### Prompt Set 3 — Algorithmic Understanding

**Variant A**
> What is the time complexity of binary search?

**Variant B**
> If I repeatedly halve the search space to find a target value in a sorted list, how does the number of steps grow relative to the list size?

**Variant C**
> Compare the worst-case number of comparisons needed to find an element using binary search versus linear search in a sorted array of n elements.

**Expected answer:** O(log n) for binary search, O(n) for linear search  
**Evaluation criteria:** Consistency, Instruction Following, Output Clarity
