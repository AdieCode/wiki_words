import re
import os
import time
from tqdm import tqdm
from memory_profiler import profile

def add_words_to_file(words):
    """
    This function recieves a list of words and adds them to a list

    @recieve (words <-- list of strings)
    @retuen  (None)
    """
    try:
        #stores the file path in variable
        path = "Datasets/words.txt"

        #if the file is not found it will create a new one 
        with open(path, "w", encoding="utf-8") as file:
            pass
        
        #Words will now get appended to the file one for one
        with open(path, "a", encoding="utf-8") as file:

            # Wrap the loop with tqdm to create the progress bar
            with tqdm(total=len(words), desc="Adding Words To File", unit="word") as pbar:
                    for word in words:
                        file.write(word+"\n")
                        pbar.update(1)

            print("words added to file...done",flush=True)
            print("",flush=True)

    #possible errors that could occur
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
    except ValueError:
        print("Incorrect value recieved.")
    except TypeError:
        print("value is unexpected type.")
    except KeyboardInterrupt:
        print("Function interrupted...")




def convert_lines_to_words(lines):
    """
    This function recieves a list of paragraffs and splits them into words
    and returns a list of words that are unfiltered.

    @recieve (lines <-- list of strings)
    @retuen  (words --> list of strings)
    """

    # Error handling checks
    try:

        #create empty list for the split_line's words to be stor
        words = []

        # Wrap the loop with tqdm to create the progress bar
        with tqdm(total=len(lines), desc="Extracting Words", unit="word") as pbar:

            #loops through the paragraphs to split the lines
            for line in lines:

                #splits the lines based on a regex pattern and adds them to words
                split_line = re.split(r'\W+', line)
                words += split_line
                pbar.update(1)
            
        print("words extracted...done",flush=True)
        print("",flush=True)
        return words
    
    #possible errors that could occur
    except ValueError:
        print("Incorrect value recieved.")
    except TypeError:
        print("value is unexpected type.")
    except KeyboardInterrupt:
        print("Function interrupted...")




def filter_words(words):
    """
    This function recieves a list of words and removes any symboles, numbers, baracets....
    and returns a list of cleaned words back.

    @recieve (words <-- list of strings)
    @retuen  (clean_words --> list of strings)
    """

    try:

        #create empty list for the clean words to be appended to.
        clean_words = []

        # Wrap the loop with tqdm to create the progress bar
        with tqdm(total=len(words), desc="Filtering Words", unit="word") as pbar:

            for word in words:

                #removes symboles an from word
                clean_word = re.sub(r'[^a-zA-Z\s]', '', word)  #word.translate({ord(i): None for i in '!?[]/:;﻿<>^~%°'})

                #adds the clean word to the new list of clean words
                if clean_word and (clean_word not in clean_words):
                    clean_words.append(clean_word)

                # Update the progress bar after processing each word
                pbar.update(1)  

    #possible errors that could occur
    except ValueError:
        print("Incorrect value recieved.")
    except TypeError:
        print("value is unexpected type.")
    except KeyboardInterrupt:
        print("Function interrupted...")


    print("words cleaned...( " + str(len(clean_words)) + " words)...done",flush=True)
    print("",flush=True)

    sorted_words = sorted(clean_words)
    return sorted_words
    

try:
    with open("Datasets/info.txt", "r", encoding="utf-8") as file:
        print("")
        start_time = time.time()
        lines = file.readlines()
        words = convert_lines_to_words(lines)
        clean_words = filter_words(words)
        add_words_to_file(clean_words)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed Time: ", round((elapsed_time / 60), 2), " minutes")
        print("")

except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
except Exception as e:
    print("An error occurred:", str(e))
