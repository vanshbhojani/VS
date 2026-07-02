
from bs4 import BeautifulSoup
import requests

html = """
<html>
<head>
    <title>Student Information</title>
</head>

<body>

    <h1 id="main_heading">Student Details</h1>

    <p class="description">
        This is a web scraping demo.
    </p>

    <div>
        <span>Name: Dishant Shah</span>
    </div>

    <a href="https://www.google.com">Google</a>

    <ul>
        <li>Python</li>
        <li>Pandas</li>
        <li>NumPy</li>
    </ul>

    <table border="1">
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>

        <tr>
            <td>Dishant</td>
            <td>25</td>
        </tr>
    </table>

</body>
</html>

"""
soup =BeautifulSoup(html,"html.parser")

title =soup.find("title")
h_tag =soup.find("h1")
div_tag=soup.find("div")
p_tag=soup.find("p").text()
href_tag=soup.find("a")['href']
ul_tag=soup.find_all("ul")
tr_tag=soup.find_all("tr")

print(title.text)
print(h_tag.text)
print(div_tag.text)
print(p_tag)
print(href_tag)

for i in soup.find_all("ul"):
    print(i.text)

for j in soup.find_all("tr"):
    print(j.text)
