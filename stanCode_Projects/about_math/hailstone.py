"""
File: hailstone.py
Name: Chun
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO: Calculation of Hailstone Sequence.
    """
    # 說明程式用途
    print('This program computes Hailstone Sequences')
    number = int(input('Enter a number: '))
    # 起始次數
    time = 0
    # 邊界條件先列出來
    if number != 1:
        while True:
            # 同一行要print新舊number，所以另外建立function再return
            number1 = number_compute(number)
            if number == 1:
                print('It took ' + str(time) + ' steps to reach 1.')
                break
            elif number % 2 == 0:
                print(str(number) + " is even, so I take half: " + str(number1))
            else:
                print(str(number) + " is odd, so I make 3n+1: " + str(number1))
            time += 1  # 成功一次就次數+1
            number = number1  # 以新number繼續loop
    else:
        print('It took 0 steps to reach 1. ')


def number_compute(number):
    if number % 2 == 0:
        number1 = int(number / 2)
    else:
        number1 = int(3 * number + 1)
    return number1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
