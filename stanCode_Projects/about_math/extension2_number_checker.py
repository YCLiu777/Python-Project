"""
File: extension2_number_checker.py
Name: Chun
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""


STOP = -100


def main():
    """
    TODO: Tell you the number is perfect or not.
    """
    print('Welcome to the number checker! ')
    while True:
        number = int(input('n: '))
        if number == STOP:
            print('Have a good one! ')
            break
        # 0一定是完美數，先獨立列出
        elif number == 0:
            print(str(number) + ' is a perfect number ')
        else:
            total = 0  # 放迴圈外，才不會一直被重置
            print(number)
            for i in range(1, number):
                if number % i == 0:
                    # print(i)  # 檢查因數是否正確
                    total = total + i
                    # print(total)  # 檢查總和是否計算正確
            if number > total:
                print(str(number) + ' is a deficient number. ')
            elif number < total:
                print(str(number) + ' is a abundant number. ')
            else:
                print(str(number) + ' is a perfect number. ')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
