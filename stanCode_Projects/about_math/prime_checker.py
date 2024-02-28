"""
File: prime_checker.py
Name: Chun
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
# Sentinel Value
EXIT = -100


import math


def main():
	"""
	TODO: The program of prime checker.
	"""
	# 說明來意
	print('Welcome to the prime checker! ')
	while True:
		number = int(input('n: '))
		if number == EXIT:
			print('Have a good one! ')
			break
		# 0、1非質數也非合數，需另外排除
		elif number <= 1:
			print(str(number) + ' is neither a prime nor composite. ')
		# 2是最小的質數，特別列出來
		elif number == 2:
			print(str(number) + ' is a prime number. ')
		else:
			for i in range(2, number):
				if number % i == 0:
					print(str(number) + ' is not a prime number. ')
					# 列出可以整除number的因數i
					# print(str(number) + ', ' + str(i))
					break
			else:
				print(str(number) + ' is a prime number. ')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
