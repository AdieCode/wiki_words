from bs4 import BeautifulSoup
import requests 
import sys
import time
from tqdm import tqdm
import os


def add_content_to_file(content):
    """
    This function recieves a list of content and adds them to a list

    @recieve (words <-- list of strings)
    @retuen  (None)
    """
    try:
        #stores the file path in variable
        path = "Datasets/info.txt"

        #if the file is not found it will create a new one 
        try:
            with open(path, "a", encoding="utf-8") as file:
                pass
        except:
            with open(path, "w", encoding="utf-8") as file:
                print("FILE CREATED (info.txt) ")
        
        #Words will now get appended to the file one for one
        with open(path, "a", encoding="utf-8") as file:

            # Wrap the loop with tqdm to create the progress bar
            with tqdm(total=len(content), desc="Adding content To File", unit="item") as pbar:
                    for item in content:
                        file.write(item+"\n")
                        pbar.update(1)

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

    print("")



def Scrape_wiki(runs):
    """
    scrapes all the paragraphs it can find on wikipidia and adds them to a list 
    and returns that list and the amount of failures and continues this until it 
    satisfies the amount of runs spicifide.

    @recieve (runs <-- amount of times scrapes preformed)
    @retuen  (list_paragraph, none_found --> paragraphs and amount of failuers)
    """

    # initilize needed variables for paragraphs to be stored
    # and searches that returned nothing.
    list_paragraphs = [] 
    none_found = 0

    #runs for the spicified amount of times requested an keeps progrees of scraping.
    for _ in tqdm(range(runs), desc="Progress", unit="Extractions"):

        #check if site returns data otherwise increase none_found.
        try :
            page_to_scrape = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        except:
            none_found += 1
            continue

        #parse the information recieved by request to beautifulsoup.
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        paragraphs = [p.text for p in soup.find_all("p") if len(p.text) > 8] 

        # if the list is not empty add it to the list.
        if paragraphs:
            list_paragraphs.extend(paragraphs)

    #return scraped paragraphs and number of faild scrapes.
    print("")
    return (list_paragraphs,none_found)




print("\n"+"Please wait for progress to reach a (100%) otherwise the data will not be stored in the textfile! { this might take a while...} " + "-"*127 + "\n")
start_time = time.time()

content_list, none_found = Scrape_wiki(1000)
add_content_to_file(content_list)

end_time = time.time()
elapsed_time = end_time - start_time

print("Scrape size : " + str(sys.getsizeof(content_list)) + " bytes")
print("None found : " + str(none_found))
print("Elapsed Time: ", round((elapsed_time / 60), 2), " minutes")

print("")
print("-------------------------------------------------------------------------------------------------------------------------------")
print("")