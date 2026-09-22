'''import requests
from bs4 import BeautifulSoup

url= "https://mega.nz/folder/AicjFarJ#TWeFzkrIrf8FW5lGMunA2g/folder/BylRhRQC"

response =requests.get(url)
soup =BeautifulSoup(response.text,"html.parser")

size_tag = soup.find_all("tr",class_="folder megaListItem ui-selectee")

for i in size_tag:
    a=size_tag.find_all("td",class_="time ad")
    for j in a:
        print(j.text.strip())


'''    
'''import requests
from bs4 import BeautifulSoup


url ="https://mega.nz/folder/AicjFarJ#TWeFzkrIrf8FW5lGMunA2g/folder/BylRhRQC"

response=requests.get(url)
soup= BeautifulSoup(response.text,"html.parser")


div_tag= soup.find_all("div",class_="grid-wrapper")
span_tag =soup.find_all("span", class_="tranfer-filetype-txt")

tb_tag= soup.select("tbody.folder megaListItem ui-selectee")

for i in div_tag:
    td_tag=i.find_all("td",class_="size")
    for j in td_tag:
        print(j.text.strip())
        # print()
'''


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()

# driver.get("https://mega.nz/folder/AicjFarJ#TWeFzkrIrf8FW5lGMunA2g/folder/BylRhRQC")

# WebDriverWait(driver,20).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME,"grid-wrapper"))
# )


# div_tag= driver.find_elements(By.CLASS_NAME,"grid-wrapper")


# for div in div_tag:
#     tbody_tag=div.find_elements(By.TAG_NAME,"tbody")
#     for tb in tbody_tag:
#         size=tb.find_element(By.CLASS_NAME,"size")
#         print(size.text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://mega.nz/folder/AicjFarJ#TWeFzkrIrf8FW5lGMunA2g/folder/BylRhRQC")

# WebDriverWait(driver,50).until(
#     EC.presence_of_all_elements_located(
#         (By.CSS_SELECTOR, "tr.folder.megaListItem")
#     )
# )

rows = driver.find_elements(By.CSS_SELECTOR, "tr.folder.megaListItem")

print("Rows found:", len(rows))

print(rows[0].get_attribute("outerHTML"))

# rows = driver.find_elements(By.CSS_SELECTOR, "tr.folder.megaListItem")

# for row in rows:
#     name = row.find_element(By.CSS_SELECTOR, "span.transfer-filetype-txt").text
#     date = row.find_element(By.CSS_SELECTOR, "td.time.ad").text
#     file_type = row.find_element(By.CSS_SELECTOR, "td.type").text
#     size = row.find_element(By.CSS_SELECTOR, "td.size").text

#     print(name, date, file_type, size)

driver.quit()