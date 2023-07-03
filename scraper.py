from bs4 import BeautifulSoup
import requests 
import sys
import time
from tqdm import tqdm

lst = []
none_found = 0
runs = 1000

print("")
print("Please wait for progress to reach a (100%) otherwise the data will not be stored in the textfile! { this might take a while...}")
print("-------------------------------------------------------------------------------------------------------------------------------")
print("")

start_time = time.time()

for _ in tqdm(range(runs), desc="Progress", unit="Extractions"):

    try :
        page_to_scrape = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        paragraphs = [p.text for p in soup.find_all("p") if len(p.text) > 8] 

        if paragraphs:
            lst.extend(paragraphs)

    except:
        none_found += 1

end_time = time.time()

elapsed_time = end_time - start_time

print("File size : " + str(sys.getsizeof(lst)) + " bytes")
print("None found : " + str(none_found))
print("Elapsed Time: ", round((elapsed_time / 60), 2), " minutes")

with open("Textfiles/info.txt", "a", encoding="utf-8") as file:
    for par in lst:
        file.write(par)
print("")
print("-------------------------------------------------------------------------------------------------------------------------------")
print("")