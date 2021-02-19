#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Edwin Dalmaijer"

import numpy

alphabet_proportions = { \
    "a":0.0854, \
    "b":0.0450, \
    "c":0.0494, \
    "d":0.0504, \
    "e":0.0306, \
    "f":0.0250, \
    "g":0.0297, \
    "h":0.0308, \
    "i":0.0192, \
    "j":0.0568, \
    "k":0.0544, \
    "l":0.0428, \
    "m":0.0824, \
    "n":0.0470, \
    "o":0.0183, \
    "p":0.0373, \
    "q":0.0039, \
    "r":0.0547, \
    "s":0.1072, \
    "t":0.0509, \
    "u":0.0072, \
    "v":0.0189, \
    "w":0.0159, \
    "x":0.0035, \
    "y":0.0187, \
    "z":0.0146, \
    }

alphabet = list(alphabet_proportions.keys())
alphabet.sort()

p = numpy.zeros(len(alphabet), dtype=float)
for i, letter in enumerate(alphabet):
    p[i] = alphabet_proportions[letter]

max_guesses = int(input("What is the maximum number of guesses?\n"))
print("\n\nStarting game with {} guesses!".format(max_guesses))
print("\n\n")

current_guess = 0
remaining_letters = list(alphabet)
while len(remaining_letters) > 1:
    p_ = numpy.copy(p)
    guess = {"a":[], "b":[]}
    current_list = "a"
    while numpy.sum(p_) > 0:
        i = numpy.argmax(p_)
        if alphabet[i] not in remaining_letters:
            p_[i] = 0
        else:
            guess[current_list].append(alphabet[i])
            if current_list == "a":
                current_list = "b"
            else:
                current_list = "a"
            p_[i] = 0
    
    response = int(input("Is letter in {}?\n(1=yes or 0=no)\n".format( \
        guess["a"])))

    if response:
        remaining_letters = guess["a"]
    else:
        remaining_letters = guess["b"]

    current_guess += 1
    
    if current_guess >= max_guesses:
        break

print("\n\nMy guess is '{}'".format(remaining_letters[0]))
