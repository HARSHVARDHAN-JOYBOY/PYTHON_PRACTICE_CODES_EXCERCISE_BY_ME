import requests

query=input("What News You want to read Enter a Topic : ")
api="b27f41ab72e54809b7d21f2dffe68978"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-10-05&sortBy=publishedAt&apiKey={api}"

print(url)
rq= requests.get(url)
data=rq.json()
articles=data["articles"]

for index,article in enumerate(articles):
    print(index + 1,article["title"],article["url"])
    print("\n************************************\n")




