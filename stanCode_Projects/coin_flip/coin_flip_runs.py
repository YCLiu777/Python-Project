"""
File: coin_flip_runs.py
Name: Chun
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO: Show the runs of coin flip.
	"""
	print('Let\'s flip a coin! ')
	number = int(input('Number of runs: '))
	outcome = ['T','H']  # 定義可以隨機抽取的集合
	coin1 = r.choice(outcome)
	# print(coin1)  # 檢查用
	coin_string = coin1
	run = 0
	is_in_a_run = False
	while True:
		coin2 = r.choice(outcome)
		# print(coin2)  # 檢查用
		if coin2 == coin1:
			if is_in_a_run == False:
				run += 1
				is_in_a_run = True
				coin_string = coin_string + coin2
				coin1 = coin2
				if run == number:
					break
		else:
			is_in_a_run = False
			coin_string = coin_string + coin2
			coin1 = coin2
	print(coin_string)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
