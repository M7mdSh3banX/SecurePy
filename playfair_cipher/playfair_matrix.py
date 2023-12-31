import numpy as np


def create_matrix(key):
    key = key.upper()
    playfair_matrix = [[0 for _ in range(5)] for _ in range(5)]
    letters_added = []

    # add the key to the matrix
    for letter in key:
        if letter not in letters_added:
            letters_added.append(letter)
        else:
            continue

    # Add the rest of the alphabet to the matrix
    for letter in range(65, 91):
        if letter == 74:  # I/J are in the same position
            continue
        if chr(letter) not in letters_added:  # Do not add repeated letters
            letters_added.append(chr(letter))

    index = 0
    for i in range(5):
        for j in range(5):
            playfair_matrix[i][j] = letters_added[index]
            index += 1
    return playfair_matrix
