from bs4 import BeautifulSoup
import requests 
import csv
import time
import random

def create_dictionary(words):
    definition_list = []
    with open("Datasets/dict.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["word","definition"])
        for word in words:
            page_to_scrape = requests.get("https://en.wikipedia.org/wiki/"+word)
            soup = BeautifulSoup(page_to_scrape.text, "html.parser")
            paragraph = soup.find_all("p")
            if paragraph:
                writer.writerow([word,paragraph[0].text])
            



with open("Textfiles/words.txt", "r", encoding="utf-8") as file:
    list_def = []
    list_words = file.readlines()
    for index in range(0,300):

        list_def.append(list_words[random.randint(0,100000)].strip("\n"))

    start_time = time.time()
    create_dictionary(list_def)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: ", round((elapsed_time / 60), 2), " minutes")