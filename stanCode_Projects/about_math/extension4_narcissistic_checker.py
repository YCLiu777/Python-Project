"""
File: extension4_narcissistic_checker.py
Name: Chun
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
    """
    TODO: Tell you whether the number narcissistic or not.
    """
    print('Welcome to the narcissistic number checker! ')
    while True:
        number = int(input('n: '))
        if number == EXIT:
            print('Have a good one! ')
            break
        else:
            calcu = cal(number)
            if number == calcu:
                print(str(number) + ' is a narcissistic number ')
            else:
                print(str(number) + ' is not a narcissistic number ')


def cal(number):
    """
    :param number: int, the number entered by user.
    :return: int, the calculation of the number.
    """
    length = len(str(number))
    total = 0
    for i in range(length, 0, -1):
        num1 = number // (10 ** (i-1))
        # print(num1)  # 檢查每個十分位數是否正確
        num2 = num1 ** length
        total += num2
        number = number - num1 * (10 ** (i-1))  # 要減掉上一個10倍數
        # print(total)  # 檢查最終加總是否正確
    return total


if __name__ == '__main__':
    main()
