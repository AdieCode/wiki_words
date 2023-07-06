import os
import pandas as pd
import matplotlib.pyplot as plt

def letter_counter(words):
    list_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for word in words:
        for letter in word:
            if letter.upper() in list_alphabet:
                list_count[list_alphabet.index(letter.upper())] += 1

    new_list = {}
    new_list["letter"] = list_alphabet
    new_list["count"] = list_count

    return new_list

with open("Datasets/words.txt", "r", encoding="utf-8") as file:
    words = file.readlines()
    df = pd.DataFrame(letter_counter(words))
    df.plot(kind='bar',x="letter",y="count", title ="Letter count in words.txt")
    plt.savefig("Figures/letter_count.png")

    