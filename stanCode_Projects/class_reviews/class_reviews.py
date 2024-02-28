"""
File: class_reviews.py
Name: Chun
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
	"""
	TODO: Show the score of the class.
	"""
	classes = input('Which class? ')
	if classes == '-1':  # 轉成文字判斷是否為離開係數
		print('No class scores were entered ')
	else:
		class_name = classes.upper()
		score = int(input('Score: '))
		if class_name == 'SC001':
			maximum001 = score
			minimum001 = score
			time001 = 1  # 第一筆成功的資料
			total001 = score   # 第一筆成功資料的總和
			avge001 = total001 / time001   # 第一筆成功資料的平均
			maximum101 = ''  # 定義另外一個課程資料為空
			minimum101 = ''
			time101 = 0
			total101 = 0
		else:
			maximum101 = score
			minimum101 = score
			time101 = 1
			total101 = score
			avge101 = total101 / time101
			maximum001 = ''
			minimum001 = ''
			time001 = 0
			total001 = 0
		while True:
			classes = input('Which class? ')
			if classes == '-1':
				break
			else:
				class_name = classes.upper()
				score = int(input('Score: '))
				if class_name == 'SC001':
					if not maximum001:
						maximum001 = score
						minimum001 = score
					if score > maximum001:
						maximum001 = score
					if score < minimum001:
						minimum001 = score
					time001 += 1
					total001 = total001 + score
					avge001 = total001 / time001
				else:
					if not maximum101:
						maximum101 = score
						minimum101 = score
					if score > maximum101:
						maximum101 = score
					if score < minimum101:
						minimum101 = score
					time101 += 1
					total101 = total101 + score
					avge101 = total101 / time101
		print('=============SC001=============')
		if maximum001:
			print('MAX(001): ' + str(maximum001))
			print('Min(001): ' + str(minimum001))
			print('Avg(001): ' + str(avge001))
		else:
			print('No score for SC001')
		print('=============SC101=============')
		if maximum101:
			print('MAX(101): ' + str(maximum101))
			print('Min(101): ' + str(minimum101))
			print('Avg(101): ' + str(avge101))
		else:
			print('No score for SC101')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
	main()
