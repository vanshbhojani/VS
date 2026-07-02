# pagination

'''
import requests
from bs4 import BeautifulSoup

base_url= "https://quotes.toscrape.com/page/{}/"

for i in range(1,11):
    url = base_url.format(i)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    div_tags = soup.find_all("div", class_="tags")

    print(f"\n------ Page {i} ------")

    for div in div_tags:
        a_tags = div.find_all("a")
        for tag in a_tags:
            print(tag["href"])

'''

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


for i in range(1, 11):
    base_url = f"https://quotes.toscrape.com/page/{i}/"


    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    span_tags = soup.select("span.text")

    print(f"\n------ Page {i} ------")

    # for span in span_tags:
    #     print(span.text)

    # time.sleep(0.5) # Delay of 0.5 seconds between requests

    small_tags = soup.select("small.author")

    # for u in small_tags:
    #     print(u.text) 

    # time.sleep(0.5) # Delay of 0.5 seconds between requests    
  
    small_tags = soup.select("small.author")
    a_tags = soup.select("a")

    for a in a_tags:
        herf =a.get("href")
        print(herf)

    time.sleep(0.5) # Delay of 0.5 seconds between requests        






