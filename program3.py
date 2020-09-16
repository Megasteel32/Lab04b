# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Quadratic Formula
# Date:        9/14/2020

# import sympy cause I hate doing math
from sympy import *

# Defining symbols for sympy to use as well as the other variables
x = Symbol('x')
a = 0
b = 0
c = 0

# Requesting user input for A B and C
a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))

# Using sympy to get the roots then print them
roots = solve(a*(x**2) + b*x + c)
print("The roots of the equation are",roots)