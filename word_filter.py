import re
import os



def add_words_to_file(words):
    """
    This function recieves a list of words and adds them to a list

    @recieve (words <-- list of strings)
    @retuen  (None)
    """
    
    #stores the file path in variable
    path = "Textfiles/words.txt"

    #if the file is not found it will create a new one 
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            pass
    
    #Words will now get appended to the file one for one
    with open(path, "a", encoding="utf-8") as file:
        for word in words:
            file.write(word+"\n")

    print("words added to file",flush=True)




def convert_lines_to_words(lines):
    """
    This function recieves a list of paragraffs and splits them into words
    and returns a list of words that are unfiltered.

    @recieve (lines <-- list of strings)
    @retuen  (words --> list of strings)
    """
    #create empty list for the split_line's words to be stor
    words = []
    
    #loops through the paragraphs to split the lines
    for line in lines:

        #splits the lines based on a regex pattern and adds them to words
        split_line = re.split(r'\W+', line)
        words += split_line
    
    print("words extracted",flush=True)
    return words




def filter_words(words):
    """
    This function recieves a list of words and removes any symboles, numbers, baracets....
    and returns a list of cleaned words back.

    @recieve (words <-- list of strings)
    @retuen  (clean_words --> list of strings)
    """
    #create empty list for the clean words to be appended to.
    clean_words = []

    for word in words:

        #removes symboles an from word
        clean_word = re.sub(r'[^a-zA-Z\s]', '', word)  #word.translate({ord(i): None for i in '!?[]/:;﻿<>^~%°'})
     
        #adds the clean word to the new list of clean words
        if clean_word and (clean_word not in clean_words):
            clean_words.append(clean_word)

    print("words cleaned",flush=True)

    sorted_words = sorted(clean_words)
    return sorted_words
        

with open("Textfiles/info.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    words = convert_lines_to_words(lines)
    clean_words = filter_words(words)
    add_words_to_file(clean_words)

