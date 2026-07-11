
import requests
import pandas as pd

url="https://jsonplaceholder.typicode.com/posts"
'''
response =requests.get(url)

data =response.json()

df= pd.DataFrame(data)
df.to_csv("posts.csv",index=False)
print(df.head())
'''

response = requests.get(url)

new_data = {
    "userId":100,
    "id":20,
    "title":"kya bolu aab me",
    "body":"chodo nahi hoga in logo se"
    }

response = requests.post(url,json=new_data)
print(response.status_code)
print(response.json())


