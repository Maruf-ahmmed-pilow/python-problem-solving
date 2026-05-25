'''
Given two numbers N and M. Print the summation of their last digits.

Input
Only one line containing two numbers N, M (0 ≤ N, M ≤ 1018).

Output
Print the answer of the problem.

Example
InputCopy
13 12
OutputCopy
5
'''

N,M = map(int, input().split())
digits_sum = (N % 10) + (M % 10) #Get the last digit of each number and sum them up %10 take the last digit of ther number
print(digits_sum)