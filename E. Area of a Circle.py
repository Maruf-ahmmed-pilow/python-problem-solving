'''
Given a number R calculate the area of a circle using the following formula:

Area = π * R2.

Note: consider π = 3.141592653.

Input
Only one line containing the number R (1  ≤  R  ≤  100).

Output
Print the calculated area, with 9 digits after the decimal point.

Example
InputCopy
2.00
OutputCopy
12.566370612
'''
π = 3.141592653
R = float(input())
area = π * R**2
print(f"{area:.9f}")