import sys
import os
import math
import string

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print(f"Error opening input file: {filename}.")
        sys.exit()

translation_table = str.maketrans(string.punctuation + string.ascii_uppercase,
                                     " " * len(string.punctuation) + string.ascii_lowercase)
                                     
def get_words_from_line_list(text):
    text = text.translate(translation_table)
    return text.split()

def count_frequency(word_list):
    D = {}
    for word in word_list:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    return D

def get_word_frequencies(filename):
    file = read_file(filename)
    word_list = get_words_from_line_list(file)
    return count_frequency(word_list)


def inner_product(D1, D2):
    sum = 0
    for key, value in D1.items():
        if key in D2:
            sum += value * D2[key]
    return sum

def vector_angle(D1, D2):
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python document_distance.py filename1 filename2")
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        D1 = get_word_frequencies(filename1)
        D2 = get_word_frequencies(filename2)
        distance = vector_angle(D1, D2)
        print(f"The distance between document1 and document2 is {distance} radians.")

if __name__ == "__main__":
    main()