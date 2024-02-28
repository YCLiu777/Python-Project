"""
File: similarity.py (extension)
Name: Chun
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO: find the similarity of DNA.
    """
    s1 = input('Please give me a DNA sequence to search: ')
    s2 = input('What DNA sequence would you like to match? ')
    l1 = len(s1)
    l2 = len(s2)
    bestmatch = match(s1, s2, l1, l2)
    print('The best match is ' + bestmatch)


def match(s1, s2, l1, l2):
    """
    :param s1: str, the sequence that entered by user.
    :param s2: str, something user wants to mapping.
    :param l1: int, the length of s1.
    :param l2: int, the length of s2.
    :return: str, the similarity one from mapping.
    """
    s1_2 = s1.upper()
    s2_2 = s2.upper()
    best = 0  # 在迴圈外建立best跟match的初始，否則放迴圈內會每次都被重置
    match = ''
    for i in range(l1-l2+1):  # 把s1切成跟s2等長的片段
        time = 0
        s3 = s1_2[i:i+l2]
        # print(s3)  # 檢查切出來的片段是否長度跟內容都正確
        for j in range(len(s3)):  # 逐字比對，相同time就+1
            if s2_2[j] == s3[j]:
                time += 1
            else:
                time += 0
        # print(time)  # 檢查比對出的次數是否正確
        if time >= best:
            best = time
            match = s3
        # print('For now, the best match is ' + match)  # 檢查一輪的最佳解是否都正確
    return match


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
