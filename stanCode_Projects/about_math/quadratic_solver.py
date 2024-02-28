"""
File: quadratic_solver.py
Name: Chun
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


import math


def main():
	"""
	TODO: Find the answer.
	"""
	print("This program is stanCode Quadratic Solver! ")
	a = int(input('Enter A: '))
	b = int(input('Enter B: '))
	c = int(input('Enter C: '))
	judgment = (b * b) - (4 * a * c)
	while True:
		if judgment == 0:
			square = math.sqrt(judgment)
			answer_1 = ((0 - b) + square) / (2 * a)
			print('One root: ' + str(answer_1))
			break
		elif judgment > 0:
			square = math.sqrt(judgment)
			answer_1 = ((0 - b) + square) / (2 * a)
			answer_2 = ((0 - b) - square) / (2 * a)
			print('Two roots: ' + str(answer_1) + ', ' + str(answer_2))
			break
		else:
			print('No real roots! ')
			break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
