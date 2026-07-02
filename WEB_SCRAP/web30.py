import requests
from bs4 import BeautifulSoup
# custom header :

# 4. custom header : 

"""
url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(response.json())
"""

# cookies example  :

"""cookies = {
    "username": "dishant"
}

"""

# hw  : cookies example , if  i accept the  cookies  then what happen  if i reject the cookies ? 

# css : function  :  select 

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# quotes = soup.select("span.text")
# quotes =soup.find_all("span",class_="text")
authors =soup.select("small.author")
tages = soup.select("div.tags")

# for i in quotes:
#     print(i.text)

# for i in authors:
#     print(i.text)

# for j in tages:
#     print(j.text)

tags_tag = soup.select("div.tags")
a_tag =soup.select("a.tag")
links_tag =soup.select("a")
text_lines = soup.select("span.text")

for i in tags_tag:
    print(i.text)

for i in a_tag:
    print(i.text)

for i in links_tag:
    print(i["href"])    

for i in text_lines:
    print(i.text)


    



# pagination :

