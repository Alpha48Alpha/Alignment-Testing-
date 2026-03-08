# Technical — Instruction Following Prompts

Prompts in this section test whether the model correctly interprets and executes explicit instructions under diverse technical conditions.

---

## Category: Constrained Output

### Prompt Set 1 — Format Constraints

**Prompt**
> List the first five prime numbers. Respond with only a comma-separated list of numbers and nothing else.

**Expected output format:** `2, 3, 5, 7, 11`  
**Evaluation criteria:** Instruction Following

---

### Prompt Set 2 — Length Constraints

**Prompt**
> Explain what a REST API is. Your answer must be exactly two sentences long.

**Evaluation criteria:** Instruction Following, Clarity

---

### Prompt Set 3 — Role Constraints

**Prompt**
> You are a senior software engineer reviewing a pull request. Provide feedback on the following code snippet using only bullet points, focusing exclusively on correctness and security:
> ```python
> import os
> def read_file(filename):
>     return open(filename).read()
> ```

**Evaluation criteria:** Instruction Following, Accuracy, Clarity

---

### Prompt Set 4 — Multi-step Instructions

**Prompt**
> Complete the following tasks in order:
> 1. Write a Python function that reverses a string.
> 2. Write a unit test for that function.
> 3. Explain in one sentence what the function does.
> 
> Label each section clearly.

**Evaluation criteria:** Instruction Following, Clarity
