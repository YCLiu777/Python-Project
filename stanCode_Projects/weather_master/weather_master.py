"""
File: weather_master.py
Name: Chun
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


import math


# This constant controls when to stop
# Sentinel Value
EXIT = -100


def main():
	"""
	TODO: Be the weather master.
	"""
	print('stanCode \"Weather Master 4.0\"! ')
	tempt = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	cold_days = 0
	if tempt == EXIT:
		print('No temperatures were entered. ')
	else:
		maximum = tempt
		minimum = tempt
		time = 1   # 第一筆成功的資料
		total = tempt   # 第一筆資料的總和
		avge = total / time   # 第一筆資料的平均
		if tempt < 16:
			cold_days += 1
		while True:
			tempt = int(input('Next Temperature: (or -100 to quit)? '))
			if tempt == EXIT:
				break
			if tempt > maximum:
				maximum = tempt
			if tempt < minimum:
				minimum = tempt
			if tempt < 16:
				cold_days += 1
			time += 1  # 成功輸入次數+1
			total = total + tempt  # 成功輸入計入總數
			avge = total / time
		print('Highest temperature = '+str(maximum))
		print('Lower temperature = '+str(minimum))
		print('Average = ' + str(avge))
		print(str(cold_days)+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
