#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

question = "What is a?:"
question2 = "What is b?:"
question3 = "What is c?:"
A = input(question)
A = float(A)
B = input(question2)
B = float(B)
C = input(question3)
C = float(C) 

x = float((C - B) / A )

print(f"Your answer is {x}")