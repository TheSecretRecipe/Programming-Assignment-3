# COP 4533 Assignment 3 - Highest Value Longest Common Subsequence

## Student Information
Name: Samaree Lewis   
UFID: 196-417-31 

## Build Instructions
Run:

make

## Run Instructions
Example:

./hvlcs < data/example.in

## Example Input
Located in:

data/example.in

## Example Output
Located in:

data/example.out

## Assumptions
- Input format follows the assignment specification.
- Character values are nonnegative integers.
- The program outputs one optimal highest-value common subsequence.
- If multiple optimal subsequences exist, any one may be printed.

## Question 1: Empirical Comparison
I tested the program on 10 nontrivial input files, each with strings of length at least 25. The runtime increased as the input sizes increased, which is consistent with the dynamic programming solution using a table of size n by m. Since each table entry is computed once in constant time, the observed runtime trend matches quadratic growth in the two string lengths.

## Question 2: Recurrence Equation
Let dp[i][j] be the maximum value of a common subsequence between the first i characters of A and the first j characters of B.

Base cases:

- dp[0][j] = 0 for all j
- dp[i][0] = 0 for all i

Recurrence:

- If A[i-1] == B[j-1], then  
  dp[i][j] = dp[i-1][j-1] + value(A[i-1])

- Otherwise,  
  dp[i][j] = max(dp[i-1][j], dp[i][j-1])

This is correct because if the characters match, we can extend an optimal solution for the smaller prefixes by adding that matching character’s value. If they do not match, then an optimal subsequence must exclude one of the two last characters, so we take the better of those two subproblems.

## Question 3: Pseudocode and Big-Oh

### Pseudocode
1. Read K and the character values
2. Read strings A and B
3. Create a 2D table dp of size (n+1) by (m+1), initialized to 0
4. For each i from 1 to n:
   - For each j from 1 to m:
     - If A[i-1] == B[j-1]:
       - dp[i][j] = dp[i-1][j-1] + value(A[i-1])
     - Else:
       - dp[i][j] = max(dp[i-1][j], dp[i][j-1])
5. Reconstruct one optimal subsequence by tracing backward from dp[n][m]
6. Print the maximum value and the subsequence

### Runtime
The runtime is O(nm) because the algorithm fills an n by m dynamic programming table and each entry takes constant time to compute.

### Space
The space complexity is O(nm) because the full dynamic programming table is stored.

## Repository Structure
- src/main.cpp
- data/example.in
- data/example.out
- data/input1.in through data/input10.in
- scripts/generate_inputs.py
- scripts/benchmark.py
- scripts/plot_runtime.py
- Makefile
- README.md
