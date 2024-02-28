"""
File: extension1_factioral.py
Name: Chun
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


STOP = -100


def main():
	"""
	TODO: Tell you the Factorial.
	"""
	print('Welcome to stanCode factorial master! ')
	while True:
		number = int(input('Give me a number, and I will list the answer of factorial: '))
		if number == STOP:
			print('- - - - - - See ya! - - - - - -')
			break
		else:
			factorial = 1
			for i in range(number, 0, -1):
				if i != 1:
					factorial = factorial * i
			else:
				print(str(factorial))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()