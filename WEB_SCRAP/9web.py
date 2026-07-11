import selenium
from selenium import webdriver
import  time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# ex :1  next button  : pagination  
"""
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")

time.sleep(4)
next_btn = driver.find_element(By.CSS_SELECTOR, "li.next a")
next_btn.click()

print(driver.title)
print(driver.current_url)

driver.quit()
"""
# ex : search  id :
'''
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

time.sleep(2)

search = driver.find_element(By.ID, "searchInput")
search.send_keys("Java programming")

search.submit()

time.sleep(3)
print(driver.title)
print(driver.current_url)
print(driver.page_source[:500])
driver.quit()
'''
'''

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

time.sleep(2)

search = driver.find_element(By.ID,"searchInput")
search.send_keys("R programing")

search.submit()

time.sleep(3)
print(driver.title)
print(driver.current_url)
print(driver.page_source[:500])
driver.quit()
'''

'''
driver =webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

time.sleep(3)

search = driver.find_element(By.ID , "searchInput")
search.send_keys("php laravel")

search.submit()

time.sleep(2)

print()

'''


import requests

url ="https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

# print("title :",data[0]['title'])

for i in data:
    print(i['title'])


