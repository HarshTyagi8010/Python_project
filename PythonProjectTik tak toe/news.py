import requests 
import json
query = input("What type of news are you interested in ?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-09-29&to=2023-09-29&sortBy=popularity&apiKey=b2fb058e41954e48b2e5e75e39552b23"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------")