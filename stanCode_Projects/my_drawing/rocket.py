"""
File: rocket.py
Name: Chun
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.
"""


# This constant determines rocket size.
SIZE = 3


def main():
    """
    TODO: Creat a cool rocket.Bui~~~
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    TODO: The rocket head created by space、\ and /.
    """
    # 火箭的寬度會是2*(SIZE+1)
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        for j in range(SIZE-i):
            print(' ', end='')
        print('')


def belt():
    """
    TODO: The rocket belt created by + and =.
    """
    print('+', end='')
    for i in range(1, 2*SIZE+1):
        print('=', end='')
    print('+', end='')
    print('')


def upper():
    """
    TODO: The upper of rocket created by |、•、\ and /.
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(SIZE-1-i):
            print('•', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-1-i):
            print('•', end='')
        for j in range(1):
            print('|', end='')
        print('')


def lower():
    """
    TODO: The lower of rocket also created by |、•、\ and /.
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('•', end='')
        for j in range(SIZE-i):
            print('\\/', end='')
        for j in range(i):
            print('•', end='')
        for j in range(1):
            print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
