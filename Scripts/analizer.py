import os
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns


def letter_counter(words):
    list_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for word in words:
        for letter in word:
            if letter.upper() in list_alphabet:
                list_count[list_alphabet.index(letter.upper())] += 1

    new_list = {}
    new_list["letter"] = list_alphabet
    new_list["Frequency"] = list_count

    return new_list



def amount_of_same_words(dict):
    """
    recieves a dictionary and creates a dataframe and counts the amount 
    of unique values and creates a figure and save's it as a svg
    """

    #creates the dataframe
    df = pd.DataFrame(dict)
    #remove \n from each row in column words
    df['words'] = df['words'].apply(lambda x: x.replace('\n', ''))

    df.value_counts().to_csv('Datasets/word_count.csv')
    



# with open("Datasets/unfilterd_words.txt", "r", encoding="utf-8") as file:
#     words = file.readlines()
#     df = pd.DataFrame(letter_counter(words))

#     df = df.sort_values(by='Frequency', ascending=True)

#     # Select the top N words
#     N = 26
#     top_words = df.head(N)

#     # Create the bar chart
#     fig, ax = plt.subplots(figsize=(5, 6))
#     ax.barh(top_words['letter'], top_words['Frequency'],color="#1977E3")


#     plt.xlabel('letter')
#     plt.ylabel('Frequency')
#     plt.title(f'Top Letters')
#     plt.savefig("Figures/letter_count_unfilterd.png")


df = pd.read_csv("Datasets/word_count.csv")
while True:
    user_word = input("Enter a word : ")
    try:
        word_count = df[df["words"] == user_word]['count'].values[0]
        print("")
        print("Found : " + str(word_count) + " times"+"\n")
    except:
        print("")
        print("word not found" + "\n")

    