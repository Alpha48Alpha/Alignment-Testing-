# Technical Prompts — Mathematics
**Domain:** Technical | **Subdomain:** Mathematics  
**Total Prompts:** 40  
**Evaluation Criteria:** mathematical rigor, step clarity, correct notation, applicability

---

## Algebra & Pre-Calculus

**M-001**  
`Solve the system of equations: 3x + 2y = 12 and x - y = 1. Show both substitution and elimination methods, then verify your solution.`  
*Tags: linear algebra, systems of equations, beginner*

**M-002**  
`Factor the polynomial 6x³ - 11x² - 10x + 8 completely. Explain each step of the factoring process.`  
*Tags: polynomials, factoring, intermediate*

**M-003**  
`Derive the quadratic formula by completing the square on ax² + bx + c = 0. Explain each algebraic manipulation.`  
*Tags: quadratic formula, derivation, intermediate*

**M-004**  
`Simplify the expression (x² - 9)/(x² + 5x + 6) and state the domain restrictions. Explain why domain matters.`  
*Tags: rational expressions, domain, intermediate*

**M-005**  
`A function f(x) = 2x³ - 5x² + 3 is given. Find all critical points and determine where the function is increasing or decreasing without calculus (using sign analysis of first differences).`  
*Tags: functions, analysis, intermediate*

---

## Calculus

**M-006**  
`Using the epsilon-delta definition, prove that lim(x→2) of (3x - 1) = 5. Walk through the logic step by step.`  
*Tags: limits, epsilon-delta, rigorous proof, advanced*

**M-007**  
`Differentiate f(x) = x² · sin(x) · e^x using the product rule. Clearly label each application of the rule.`  
*Tags: differentiation, product rule, chain rule, intermediate*

**M-008**  
`Evaluate the integral ∫ x·ln(x) dx using integration by parts. Verify your answer by differentiating.`  
*Tags: integration, integration by parts, intermediate*

**M-009**  
`Find the area bounded between the curves y = x² and y = 2x + 3. Draw a rough sketch and explain the setup.`  
*Tags: definite integrals, area between curves, intermediate*

**M-010**  
`Apply L'Hôpital's Rule to evaluate lim(x→0) of (sin(3x) / 5x). Then verify using the small-angle approximation.`  
*Tags: L'Hôpital's Rule, limits, intermediate*

**M-011**  
`Find the Taylor series expansion of e^x centered at x = 0 up to the 5th degree term. Then use it to estimate e^0.1 and compare with the true value.`  
*Tags: Taylor series, approximation, advanced*

**M-012**  
`Solve the differential equation dy/dx = 2xy with the initial condition y(0) = 3. Use separation of variables.`  
*Tags: differential equations, separation of variables, intermediate*

**M-013**  
`Find all local maxima and minima of f(x) = x⁴ - 8x² + 3 using the first and second derivative tests.`  
*Tags: optimization, derivative tests, intermediate*

---

## Statistics & Probability

**M-014**  
`A bag contains 5 red, 3 blue, and 2 green marbles. If 2 marbles are drawn without replacement, what is the probability both are red? Solve using combinations.`  
*Tags: probability, combinations, without replacement, beginner*

**M-015**  
`Explain the Central Limit Theorem with an example. Why is it important for statistical inference, even when the original distribution is not normal?`  
*Tags: CLT, statistical inference, conceptual, intermediate*

**M-016**  
`A normally distributed dataset has mean μ = 70 and standard deviation σ = 10. Find the probability that a randomly selected value falls between 60 and 85. Use the standard normal table.`  
*Tags: normal distribution, z-scores, intermediate*

**M-017**  
`Derive Bayes' Theorem from the definition of conditional probability. Then apply it to a medical testing scenario with a 1% prevalence rate and 95% test accuracy.`  
*Tags: Bayes' theorem, conditional probability, advanced*

**M-018**  
`Explain the difference between a Type I and Type II error in hypothesis testing. Give a real-world example where each type of error is especially costly.`  
*Tags: hypothesis testing, error types, conceptual, intermediate*

**M-019**  
`Perform a chi-squared goodness-of-fit test on observed vs. expected dice roll frequencies (100 rolls of a fair die). Interpret the result.`  
*Tags: chi-squared test, hypothesis testing, intermediate*

**M-020**  
`Compute the correlation coefficient between two datasets: X = [2,4,6,8] and Y = [3,5,4,7]. Interpret the result.`  
*Tags: correlation, statistics, intermediate*

---

## Linear Algebra

**M-021**  
`Compute the matrix product AB where A = [[1,2],[3,4]] and B = [[5,6],[7,8]]. Then find A·B − B·A and comment on commutativity.`  
*Tags: matrix multiplication, commutativity, beginner*

**M-022**  
`Find the inverse of the 3×3 matrix [[2,1,0],[1,3,1],[0,1,2]] using Gaussian elimination (row reduction). Verify by multiplying A · A⁻¹.`  
*Tags: matrix inverse, Gaussian elimination, intermediate*

**M-023**  
`Find the eigenvalues and eigenvectors of the matrix [[4,1],[2,3]]. Explain the geometric meaning of eigenvectors.`  
*Tags: eigenvalues, eigenvectors, intermediate*

**M-024**  
`Explain what it means for a set of vectors to be linearly independent. Give a 3×3 example and determine independence using the determinant.`  
*Tags: linear independence, determinant, intermediate*

**M-025**  
`Describe the four fundamental subspaces of a matrix (column space, null space, row space, left null space). Give an example with a 2×3 matrix.`  
*Tags: subspaces, fundamental theorem, advanced*

---

## Discrete Mathematics

**M-026**  
`Prove by mathematical induction that the sum of the first n positive integers is n(n+1)/2. Show the base case, inductive hypothesis, and inductive step.`  
*Tags: induction, proof, beginner*

**M-027**  
`How many ways can 5 students be arranged in a line? Then, how many ways can 3 be chosen from 5 for a committee (order doesn't matter)? Distinguish permutations from combinations.`  
*Tags: combinatorics, permutations, combinations, beginner*

**M-028**  
`Find the greatest common divisor (GCD) of 252 and 198 using the Euclidean algorithm. Show every step.`  
*Tags: number theory, Euclidean algorithm, beginner*

**M-029**  
`Explain the Pigeonhole Principle with two original examples: one simple, one non-obvious. State the generalized form.`  
*Tags: pigeonhole principle, combinatorics, intermediate*

**M-030**  
`Construct a truth table for the compound proposition (P ∧ Q) → (¬P ∨ R). Determine whether it is a tautology.`  
*Tags: logic, truth tables, propositional logic, beginner*

---

## Applied Mathematics

**M-031**  
`Model the growth of a bacterial population using an exponential function. If it doubles every 3 hours and starts at 500 cells, how many cells are there after 12 hours?`  
*Tags: exponential growth, modeling, beginner*

**M-032**  
`A ball is thrown upward with initial velocity 20 m/s from a height of 1.5 m. Using kinematics, find the maximum height and the time to hit the ground.`  
*Tags: kinematics, quadratic equations, applied, beginner*

**M-033**  
`Explain the concept of a Nash equilibrium using the Prisoner's Dilemma. What does it mean for both players to have no incentive to deviate?`  
*Tags: game theory, Nash equilibrium, intermediate*

**M-034**  
`Use linear programming (graphical method) to maximize profit P = 5x + 4y subject to: 6x + 4y ≤ 24, x + 2y ≤ 6, x ≥ 0, y ≥ 0.`  
*Tags: linear programming, optimization, intermediate*

**M-035**  
`Explain Fourier series and how any periodic function can be expressed as a sum of sines and cosines. Give the formula and a simple worked example.`  
*Tags: Fourier series, periodic functions, advanced*

---

## Number Theory

**M-036**  
`Prove that √2 is irrational using proof by contradiction. What does this tell us about the structure of real numbers?`  
*Tags: irrational numbers, proof by contradiction, beginner*

**M-037**  
`Explain Fermat's Little Theorem and show how it is used in the RSA encryption algorithm.`  
*Tags: number theory, RSA, cryptography, advanced*

**M-038**  
`Find all solutions to the congruence 3x ≡ 7 (mod 11) using modular inverse. Show the calculation.`  
*Tags: modular arithmetic, congruences, intermediate*

**M-039**  
`Explain the distribution of prime numbers and state the Prime Number Theorem. How does it approximate π(n) (the count of primes up to n)?`  
*Tags: prime numbers, Prime Number Theorem, advanced*

**M-040**  
`Compute 7^100 mod 13 using Fermat's Little Theorem and repeated squaring. Show all modular arithmetic steps.`  
*Tags: modular exponentiation, number theory, intermediate*
