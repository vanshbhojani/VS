import requests
from bs4 import BeautifulSoup

# url="https://quotes.toscrape.com/page/1/"

# response = requests.get(url)
# soup = BeautifulSoup(requests.get(url).text,"html.parser")

# # div_tag=soup.find("div",class_="quote")

# link_tag=soup.find("a",class_="tag")

# author_tag=soup.find_all("small",class_="author")

# text_tag=soup.find_all("span",class_="text")

# tage_tag=soup.find_all("div",class_="tag")

# for i in soup.find_all("div",class_="quote"):
#     print(i.text)

# for i in soup.find_all("small",class_="author"):
#     print(i.text)

# for i in soup.find_all("span",class_="text"):
#     print(i.text)
 
# print(link_tag['href'])

# for j in soup.find_all("a",class_="tag"):
#     print(j)

# for i in soup.find_all("div",class_="tags"):
#     print(i.text)


# url="https://webscraper.io/test-sites"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")


# h2_tag =soup.find("h2",class_="site-heading")
# full_site_tag =soup.find("div",class_="container test-sites")
# products_tag =soup.find("div",class_="col-lg-3")

# footer_tag =soup.find_all("div",class_="col-lg-3")

# ul_tag =soup.find_all("ul",class_="smedia")
# a_tag =soup.find("a")

# div_tag =soup.find_all("div",class_="side-collapse")

# print(full_site_tag.text)
# print(h2_tag.text)
# print(products_tag)

# print(footer_tag)

# print(ul_tag)
# print(a_tag['href'])

# for ul in ul_tag:
#     a_tag=ul.find_all("a") # a 
#     for a in a_tag:
#         print(a['href'])

# for i in soup.find_all("h2",class_="site-heading"):
    # print(i.text)

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# h1_tag =soup.find("h1",class_="title is-1")
# p_tag =soup.find("p",class_="subtitle is-3")

# print(h1_tag.text)
# print(p_tag.text)

'''
div_columns_multiline =soup.find_all("div",class_="columns is-multiline")
div_colum_heaf =soup.find_all("div",class_="column is-half")


for i in div_columns_multiline:
    div_colum_heaf =i.find_all("div",class_="column is-half")
    for j in div_colum_heaf:
        print(j.text)
'''
'''
div_columns_multiline =soup.find_all("div",class_="columns is-multiline")
footer_tag =soup.find("footer",class_="card-footer")    
a_tag =soup.find_all("a")


for i in footer_tag:
    a_tag = footer_tag.find_all("a")
    for j in a_tag:
        print(j['href'])
        '''

'''
for i in div_columns_multiline:
    footer_tag = i.find_all("footer",class_="card-footer")
    for j in footer_tag:
        a_tag = j.find_all("a")
        for k in a_tag:
            print(k['href'])

            with open("links.txt","a") as f:
                f.write(k['href'] + "\n")
'''

'''
div_columns_multiline =soup.find_all("div",class_="columns is-multiline")
div_media_content =soup.find_all("div",class_="media-content")
h2_tag =soup.find_all("h2",class_="title is-5")

if h2_tag:
    for i in div_columns_multiline:
        div_media_content = i.find_all("div",class_="media-content")
        for j in div_media_content:
            h2_tag = j.find_all("h2",class_="title is-5")
            for k in h2_tag:
                with open("job_title.txt","a")as f:
                    f.write(k.text + "\n")
    print("Job titles have been written to job_title.txt")
else:  
    print("No job titles found.")                      
'''

div_columns_multiline =soup.find_all("div",class_="columns is-multiline")
div_media_content =soup.find_all("div",class_="media-content")
h2_tag =soup.find_all("h2",class_="title is-5")
h3_tag =soup.find_all("h3",class_="subtitle is-6 company")


if h3_tag:
    for i in div_columns_multiline:
        div_media_content = i.find_all("div",class_="media-content")
        for j in div_media_content:
            h2_tag = j.find_all("h2",class_="title is-5")
            h3_tag = j.find_all("h3",class_="subtitle is-6 company")
            for k in h2_tag:
                for l in h3_tag:
                    with open("job_title_company.txt","a")as f:
                        f.write(k.text + " - " + l.text + "\n")
    print("Job titles and company names have been written to job_title_company.txt")
else:
    print("No job titles or company names found.")


