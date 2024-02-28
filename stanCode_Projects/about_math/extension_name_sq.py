"""
File: name_sq.py (extension)
Name: Chun
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    TODO: Make your name frame.
    """
    print('This program prints a name in a square pattern! ')
    name = input('name: ')
    number = len(name)
    print(name)
    # 頭尾另外寫, 所以中間迴圈的長度會是number-2
    for i in range(1, number-1):
        for j in range(1):
            print(name[i], end='')
        for j in range(number-2):
            print(' ', end='')
        for j in range(1):
            print(name[number-i-1], end='')
        print('')
    print(reverse(name, number))


def reverse(name, number):
    """
    :param name: str, the word that entered by user.
    :param number: int, the length of name.
    :return: str, the reverse word from name.
    """
    reverse = ''
    for i in range(number):
        reverse = name[i] + reverse
    return reverse


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
