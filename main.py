from bs4 import BeautifulSoup
import requests 
import sys

lst = []
count = 0
divider = 0
print("progress : [",end="",flush=True)

none_found = 0
while count < 100:

    try :
        page_to_scrape = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        sooup = BeautifulSoup(page_to_scrape.text, "html.parser")
        paragraph = sooup.find_all("p")
        if paragraph and len(paragraph[0].text) >8:
            count += 1
            lst.append(paragraph[0].text)
        if count > divider:
            divider += 10
            print("█",end="",flush=True)
    except:
         none_found += 1
         

print("]__100%__ " +(str(sys.getsizeof(lst)) + " bytes"))

print("None found : " + str(none_found))

with open("info.txt", "a", encoding="utf-8") as file:
    for par in lst:
        if len(par) > 0:
            file.write(par)

