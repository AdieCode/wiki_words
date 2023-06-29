from bs4 import BeautifulSoup
import requests 

page_to_scrape = requests.get("http://quotes.toscrape.com/")
sooup = BeautifulSoup(page_to_scrape.text, "html.parser")
qouts = sooup.find_all("span", attrs={"class":"text"})
authors = sooup.find_all("small", attrs={"class":"author"})

lst = []
for i in qouts:
    lst.append(i.text)

print(lst)


