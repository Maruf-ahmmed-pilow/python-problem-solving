'''Given two numbers X and Y. Print the summation and multiplication and subtraction of these 2 numbers.

Input
Only one line containing two separated numbers X, Y (1  ≤  X, Y  ≤  105).

Output
Print 3 lines that contain the following in the same order:

"X + Y = summation result" without quotes.
"X * Y = multiplication result" without quotes.
"X - Y = subtraction result" without quotes.
Example
InputCopy
5 10
OutputCopy
5 + 10 = 15
5 * 10 = 50
5 - 10 = -5 '''
X,Y = map(int, input().split())
summation = X + Y
multiplication = X * Y
subtraction = X - Y
print(f"{X} + {Y} = {summation}")
print(f"{X} * {Y} = {multiplication}")
print(f"{X} - {Y} = {subtraction}")