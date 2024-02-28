"""
File: hangman.py
Name: Chun
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: Guess right or died tight, extension.
    """
    print('The word looks like: ', end='')
    ans = random_word()
    for i in range(len(ans)):
        print('-', end='')
    print('')
    # print(ans)   # 檢查答案
    word1 = '-'*len(ans)
    # print(word1)  # 檢查hidden word的長度是否正確
    time = N_TURNS
    print('You have ' + str(N_TURNS) + ' wrong guesses left. ')
    if time == 7:
        time7()
    while True:
        user_guess = input('Your guess: ')
        if user_guess.isalpha():
            if len(user_guess) == 1:
                user_guess2 = user_guess.upper()
                if user_guess2 in ans:
                    print('Your are correct! ')
                    word2 = replace(ans, word1, user_guess2)
                    word1 = word2
                    # 完全猜對的最後一步
                    if word1 == ans:
                        print('You win!! ')
                        print('The answer is: ' + word1)
                        break
                    # 猜對了，但還沒完全解謎的情況
                    else:
                        print('The word look like: '+ word1)
                        print('You have ' + str(time) + ' wrong guesses left. ')
                else:
                    print('There is no ' + user_guess + "'s in the word. ")
                    time -= 1
                    # 猜錯了，但還有嘗試次數的
                    if time > 0:
                        print('You have ' + str(time) + ' wrong guesses left. ')
                        if time == 6:
                            time6()
                        elif time == 5:
                            time5()
                        elif time == 4:
                            time4()
                        elif time == 3:
                            time3()
                        elif time == 2:
                            time2()
                        else:
                            time1()
                    # 猜錯了，但已經沒機會的
                    else:
                        print('You are completely hung :( ')
                        print('The answer is: ' + word1)
                        time0()
                        break
            else:
                print('Illegal format. ')
        else:
            print('Illegal format. ')


def replace(ans, word1, user_guess2):
    """
    :param ans: str, the answer created by random_word().
    :param word1: str, the hidden word.
    :param user_guess2: str, the guess from user.
    :return word2: str, the result been guess from hidden word.
    """
    word2 = ""
    i = 0
    while True:
        i = ans.find(user_guess2)
        if i == -1:
            break
        word2 += word1[:i]
        word2 += user_guess2
        ans = ans[i + 1:]   # 往後判斷是否還有相同的字母
        word1 = word1[i + 1:]
    word2 += word1[i + 1:]
    return word2


def time7():
    """
    TODO: the hangman when left time is 7.
    """
    shelf_top_empty()
    shelf_body_feet()
    shelf_body_feet()
    shelf_lower()


def time6():
    """
    TODO: the hangman when left time is 6.
    """
    shelf_top_head()
    head()
    shelf_body_feet()
    shelf_body_feet()
    shelf_lower()


def time5():
    """
    TODO: the hangman when left time is 5.
    """
    shelf_top_head()
    head()
    body()
    shelf_body_feet()
    shelf_lower()


def time4():
    """
    TODO: the hangman when left time is 4.
    """
    shelf_top_head()
    head()
    left_hand()
    shelf_body_feet()
    shelf_lower()


def time3():
    """
    TODO: the hangman when left time is 3.
    """
    shelf_top_head()
    head()
    right_hand()
    shelf_body_feet()
    shelf_lower()


def time2():
    """
    TODO: the hangman when left time is 2.
    """
    shelf_top_head()
    head()
    right_hand()
    left_foot()
    shelf_lower()


def time1():
    """
    TODO: the hangman when left time is 1.
    """
    shelf_top_head()
    head()
    right_hand()
    right_foot()
    shelf_lower()


def time0():
    """
    TODO: the hangman when there's no more time left.
    """
    shelf_top_head()
    head_x()
    right_hand()
    right_foot()
    shelf_lower()


def shelf_top_empty():
    """
    TODO: The top of shelf created by space and |.
    """
    for i in range(16):
        print('_', end='')
    print('')
    print('|            |')


def shelf_top_head():
    """
    TODO: The top of shelf when head be hang.
    """
    for i in range(16):
        print('_', end='')
    print('')
    print('|          __|__')


def head():
    """
    TODO: The head of hangman.
    """
    print('|        /       \\')
    print('|       |         |')
    print('|        \\ _____ /')


def head_x():
    """
    TODO: The dead face of hangman.
    """
    print('|        /       \\')
    print('|       | X     X |')
    print('|        \\ _____ /')


def body():
    """
    TODO: The body of hangman.
    """
    for i in range(3):
        print('|            |  ')


def left_hand():
    """
    TODO: The body and left hand of hangman.
    """
    print('|            |\\  ')
    print('|            | \\ ')
    print('|            |  \\')


def right_hand():
    """
    TODO: The both hands and body of hangman.
    """
    print('|           /|\\  ')
    print('|          / | \\ ')
    print('|         /  |  \\')


def left_foot():
    """
    TODO: The left foot of hangman.
    """
    print('|             \\  ')
    print('|              \\ ')
    print('|               \\')


def right_foot():
    """
    TODO: The feet of hangman.
    """
    print('|           / \\  ')
    print('|          /   \\ ')
    print('|         /     \\')


def shelf_body_feet():
    """
    TODO: The shelf when body or feet is empty.
    """
    for i in range(3):
        print('|')


def shelf_lower():
    """
    TODO: The lower of shelf.
    """
    print('|')
    print('|_')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
