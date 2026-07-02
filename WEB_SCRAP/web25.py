"""
1.get : req.get(URL)  ===>https://jsonplaceholder.typicode.com/posts 
	print(status_code)
	print(respo.json()[0])

2. get  with parameter : req.get(url,params=params)
	params = {
    "userId": 1
}
	print(res.url) print(res.json())

3. post : 
	data  = {
	"title": "Python",
    "body": "Learning Requests Library",
    "userId": 1
	}

req.post(url,json=data)

4. custom header : 

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US"
}

5. cookies example  : 
cookies = {
    "username": "dishant"
}

6. 
Session stores login information and cookies.

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 301  | Redirect     |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |
| 500  | Server Error |

"""
import requests
from bs4 import BeautifulSoup
# get : using  URL to fetch data . 

"""url ="https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(response.json()[0])
"""
# get  with parameter : using  URL to fetch data .

"""
url ="https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 10
}
response = requests.get(url,params=params)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(response.json())
"""

'''post : 

url ="https://jsonplaceholder.typicode.com/posts"

data  = {
	"title": "Python",
    "body": "Learning Requests Library",
    "userId": 1
	}

reponse = requests.post(url,json=data)
soup = BeautifulSoup(reponse.text, "html.parser")

print(reponse.status_code)
print(reponse.json())

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(response.json()[10])'''

url ="https://jsonplaceholder.typicode.com/posts"

'''params = {
    "id":2
}

response = requests.get(url,params=params)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(response.json())
'''

data = {
    "title": "Python",
    "id": 10
}

response = requests.post(url,json=data)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(response.json())


