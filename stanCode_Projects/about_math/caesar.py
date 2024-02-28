"""
File: caesar.py
Name: Chun
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: The secret behind us.
    """
    secret_code = int(input('Secret number: '))
    ciphered_word = input('What\'s the the ciphered string? ')
    print(word_decipher(ciphered_word, secret_code))


def word_decipher(ciphered_word, secret_code):
    """
    :param ciphered_word: str, the string that inserted by user.
    :param secret_code: int, the key value of the secret.
    :return: str, the outcome.
    """
    decipherd_word = ""
    # 都轉大寫才能跟ALPHABET比對
    ciphered_word2 = ciphered_word.upper()
    while True:
        for ch in ciphered_word2:
            i = ALPHABET.find(ch)
            if i >= 0:
                decipherd_word += ALPHABET[order(secret_code, i)]
            # 讓非字母也要照舊顯示
            else:
                decipherd_word += ch
        return decipherd_word


def order(secret_code, i):
    """
    :param secret_code: int, the key value of the secret.
    :param i: int, the word's address in ALPHABET.
    :return: str, the current order.
    """
    # 不能出現-1
    if (len(ALPHABET) - secret_code - i) == 0:
        order = len(ALPHABET) - secret_code - i
    elif(len(ALPHABET) - secret_code - i) < 0:
        order = secret_code + i - len(ALPHABET)
    else:
        order = secret_code + i
    return order


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
