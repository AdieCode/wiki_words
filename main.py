from bs4 import BeautifulSoup
import requests 
import sys

lst = []
count = 0
none_found = 0
runs = 1000

print("")
print("(Please wait for progress to reach a 100.0 % otherwise the data will not be stored !!)")

while count < runs:
    print("Progress : [ ",str(round((count/runs)*100,2)) + " % ]", end='\r',flush=True)
    try :
        page_to_scrape = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        sooup = BeautifulSoup(page_to_scrape.text, "html.parser")
        paragraph = sooup.find_all("p")
        if paragraph and len(paragraph[0].text) >8:
            count += 1
            lst.append(paragraph[0].text)
    except:
         none_found += 1
         
print("Progress : [ ",str(round((count/runs)*100,2)) + " % ", end='')
print(" ] " + "(" + str(sys.getsizeof(lst)) + " bytes" + ")")

print("None found : " + str(none_found))

with open("info.txt", "a", encoding="utf-8") as file:
    for par in lst:
        if len(par) > 0:
            file.write(par)
print("")