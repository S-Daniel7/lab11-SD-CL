import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b
def sub (a,b):
    return a - b
def mul (a,b):
    return a * b
def div(a,b):
    try:
       return b/a
    except ZeroDivisionError:
        print("Cannot divide by Zero")
def log (a,b):
    try:
        return math.log(a,b)
    except ValueError:
        print("Number is not valid")

def exp (a,b):
    return math.pow(a,b)
