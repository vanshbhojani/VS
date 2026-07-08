#Q1. Open the Laptops page in your browser. Use DevTools (F12) to inspect the HTML. Identify the tag and class name used for: product name, price, description, star rating, and number of reviews.


'''
product_name = H4_tag  class_name = "title"
price =H4_tag  class_name = "price float-end card-title pull-right"
description = p_tag  class_name = "description card-text"
star_rating = p_tag  data-rating={}
number_of_reviews = p_tag  class_name = "review-count float-end"
'''


#Q2. Look at the site's URL structure. What changes in the URL when you go to page 2 of the Laptops section?


'''base_url = https://webscraper.io/test-sites/e-commerce/allinone
https://webscraper.io/test-sites/e-commerce/allinone/computers
https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops
https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets
https://webscraper.io/test-sites/e-commerce/allinone/phones
https://webscraper.io/test-sites/e-commerce/allinone/phones/touch

most changes in url is after /e-commerce/allinone and changes are computers, laptops, tablets, phones, touch. 
page 2 of laptops section is https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page=2 next page is https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page=3 and so on.
'''


# Q3. Write a Python script to fetch the Laptops page and print the HTTP status code and the page .
'''
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/"

response = requests.get(url)

# Print HTTP status code
print("Status Code:", response.status_code)

# Print HTML content of the page
print(response.text)

'''

# Q4. Parse the response HTML with BeautifulSoup. Count and print how many product cards exist on the first page.

'''
import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

div_tag = soup.find_all("div", class_="row")
div_tag = soup.select("div.row")

print("Number of product cards on the first page:", len(div_tag))
print(div_tag)

'''


# Q5. Make a GET request to the Laptops page with a custom User-Agent header. Print the status code and confirm the page loaded successfully.
'''
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

headers = {
    "user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}

response = requests.get(url ,headers=headers)

# Print HTTP status code
print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Page loaded successfully.")

else:
    print("Failed to load the page.")   
'''

# Q6. Use requests.Session() to make the request. Print all headers sent with the request.
'''
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

session = requests.Session()


session.headers.update = {
    "user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
    }

response = session.get(url)

print("status code:",response.status_code)
print("\n Headers sent with the request:")

for key,value in response.request.headers.items():
    print(f"{key}:{value}")
'''

# Q7. Using find_all(), extract the name of every laptop on the first page. Print all names as a list.

'''
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

respone=requests.get(url)
soup=BeautifulSoup(respone.text,"html.parser")

leptop_name= soup.find_all("a", class_="title")

laptop_name_list = []

for name in leptop_name:
    laptop_name_list.append(name.text.strip())

print(laptop_name_list)    
'''

# Q8. Using find_all(), extract the price of every laptop on the first page. Print all prices as a list.
'''
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

laptop_price = soup.find_all("h4", class_="price float-end card-title pull-right")

laptop_price_list = []

for price in laptop_price:
    laptop_price_list.append(price.text.strip())

print(laptop_price_list)

'''

# Q9. Using find_all(), extract the description of every laptop on the first page. Print first 3 descriptions.

'''
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

respeonse = requests.get(url)
soup = BeautifulSoup(respeonse.text,"html.parser")

description = soup.find_all("p",class_="description card-text")

for desc in description[:3]:
    print(desc.text.strip())
'''  


# Q10. Using find_all(), extract the star rating (number of stars) and review count for each laptop.Print both as lists.
'''
import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response =requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

star_ratings = soup.find_all("div", class_="ratings")

review_counts = soup.find_all("p", class_="review-count float-end")

print("Star Ratings:")
star_rating_list = []

for rating in star_ratings:
    stars =rating.find_all("span", class_="ws-icon ws-icon-star")
    star_rating_list.append(len(stars))

print(star_rating_list)

print("\nReview Counts:")
review_count_list = []
for review in review_counts:
    review_count_list.append(review.text.strip())

print(review_count_list)    
    
list_of_laptops = []

for i in range(len(star_rating_list)):
    info ={
        "star_rating": star_rating_list[i],
        "review_count": review_count_list[i]
    }
    list_of_laptops.append(info)

print("\nList of Laptops with Star Ratings and Review Counts:")
print(list_of_laptops)
'''

# Q11. Using CSS selectors with select(), extract the href link of every product on the page. Print the first 5 full URLs.

'''
import requests
from bs4 import BeautifulSoup

ulr = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response =requests.get(ulr)
soup = BeautifulSoup(response.text,"html.parser")

links =soup.select("a.title")

for i in links[:5]:
    href = i.get("href")
    full_url = "https://webscraper.io" + href
    print(full_url)
'''

# Q12. Identify the pagination pattern for the Laptops section. Write out the URL for page 1, 2, and 3.

'''
for i in range(1, 4):
    url = f"https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={i}"
    print(f"Page {i} URL: {url}")
'''
# or 

'''
base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={i}"

for a in range(1,4):
    url =base_url.format(i=a)
    print(url)
'''

# Q13. Write a loop to scrape laptop name and price from all available pages in the Laptops section.
# Add time.sleep(1) between requests. Store results in a list of dictionaries.
'''
import requests
from bs4 import BeautifulSoup
import time

base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={i}"

laptop_list = []

for a in range(1,7):
    url =base_url.format(i=a)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    laptop_name = soup.find_all("a", class_="title")
    laptop_price = soup.find_all("h4", class_="price float-end card-title pull-right")

    print(f"\n------ Page {a} ------")

    for i in range(len(laptop_name)):
        laptop_info = {
            "name": laptop_name[i].text.strip(),
            "price": laptop_price[i].text.strip()
        }
        laptop_list.append(laptop_info)
        print(laptop_info)

    time.sleep(1)  # Delay of 1 second between requests 

print(laptop_list)
    
'''
# use zip function to combine the laptop names and prices into a list of dictionaries.
'''
zip 

for name,price in zip(laptop_name,laptop_price):
    laptop_info ={
    "name": name.text.strip(),
    "price": price.text.strip()
    }
    laptop_list.append(laptop_info)
'''


# Q14. After scraping all pages, save the collected data to a CSV file named laptops_data.csv.

'''
import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={i}"

laptop_list = []

for a in range(1,7):
    url =base_url.format(i=a)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    laptop_name = soup.find_all("a", class_="title")
    laptop_price = soup.find_all("h4", class_="price float-end card-title pull-right")

    print(f"\n------ Page {a} ------")

    for name,price in zip(laptop_name,laptop_price):
        laptop_info ={
        "name": name.text.strip(),
        "price": price.text.strip()
        }
        laptop_list.append(laptop_info)

    time.sleep(1)  # Delay of 1 second between requests 

# print(laptop_list)
if laptop_list:    
    with open("laptops_data.csv","w",newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerows(laptop_list)
    print("Data saved to laptops_data.csv successfully.")
else:
    print("No data to save.")
'''


# Q15. Final Challenge: Scrape BOTH the Laptops and Phones sections. Collect name, price, description, rating, reviews for all products from all pages.
# Add a 'category' column. Save to ecommerce_data.csv.
'''
import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URLs
base_urls = {
    "Laptops": "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={}",
    "Phones": "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch?page={}"
}

# Store all data
all_products = []

# Loop through both categories
for category, base_url in base_urls.items():

    print(f"\nScraping {category}...")

    # Pages 1 to 6
    for page in range(1, 7):

        url = base_url.format(page)
        print(f"Page {page}: {url}")

        response = requests.get(url)

        if response.status_code != 200:
            print("Failed to load page")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Each product card
        products = soup.select("div.thumbnail")

        for product in products:

            # Name
            name = product.select_one("a.title").text.strip()

            # Price
            price = product.select_one("h4.price").text.strip()

            # Description
            description = product.select_one("p.description").text.strip()

            # Reviews
            reviews = product.select_one("p.review-count").text.strip()

            # Rating (count stars)
            rating = len(product.select("span.ws-icon-star"))

            # Store data
            all_products.append([
                category,
                name,
                price,
                description,
                rating,
                reviews
            ])

        # Delay to avoid sending requests too fast
        time.sleep(1)

# Save to CSV
with open("ecommerce_data.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Category",
        "Name",
        "Price",
        "Description",
        "Rating",
        "Reviews"
    ])

    writer.writerows(all_products)

print("\nData saved successfully!")
print(f"Total products scraped: {len(all_products)}")

'''


import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# div_tag = soup.find_all("div", class_="row")
div_tag = soup.select("div.row")

# print("Number of product cards on the first page:", len(div_tag))
print(div_tag)



