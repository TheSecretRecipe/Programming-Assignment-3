# COP 4533 Assignment 3 - HVLCS

## Build
make

## Run
./hvlcs < data/example.in

## Question 1
Runtime grows quadratically with input size. Empirical tests confirm O(nm) behavior.

## Question 2
dp[i][j] = 0 if i=0 or j=0  
if A[i] == B[j]: dp[i][j] = dp[i-1][j-1] + v(A[i])  
else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])  

## Question 3
Runtime: O(nm)  
Space: O(nm)
