from bs4 import BeautifulSoup
import requests 
import sys
import time

lst = []
count = 0
none_found = 0
runs = 100
#█ ▌
print("")
print("Please wait for progress to reach a (100.0%) otherwise the data will not be stored in the textfile!!")
print("----------------------------------------------------------------------------------------------------")
print("")

start_time = time.time()

while count < runs:
    percentig = (count/runs)
    print("Progress : [ ",str(round(percentig*100,2)) + "% ] ", ("▌" * (round(percentig * 10) - 1)) + ("-"*(10 - round(percentig*10)) ), end='\r',flush=True)
    try :
        page_to_scrape = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        paragraph = soup.find_all("p")
        if paragraph:
            count += 1
            for sentence in range(len(paragraph)):
                    lst.append(paragraph[sentence].text)

    except:
        none_found += 1

end_time = time.time()

elapsed_time = end_time - start_time
         
print("Progress : [ ",str(round((count/runs)*100,2)) + " % ", end='')
print(" ] " + "(" + str(sys.getsizeof(lst)) + " bytes" + ")" , ("▌" * round(percentig * 10)) )
print("None found : " + str(none_found))
print("Elapsed Time: ", round((elapsed_time / 60), 2), " minutes")

with open("Textfiles/info.txt", "a", encoding="utf-8") as file:
    for par in lst:
        if len(par) > 0:
            file.write(par)
print("")
print("----------------------------------------------------------------------------------------------------")
print("")