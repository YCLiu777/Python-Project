"""
File: complement.py
Name: Chun
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO: Build the complement of DNA.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, the strand of DNA to be told.
    :return dna2: str, the complement of DNA to be sloved.
    """
    dna2 = ""
    if dna != '':
        for i in range(len(dna)):
            if dna[i] == 'A':
                dna2 += 'T'
            elif dna[i] == 'T':
                dna2 += 'A'
            elif dna[i] == 'G':
                dna2 += 'C'
            else:
                dna2 += 'G'
        return dna2
    return 'DNA strand is missing. '


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
