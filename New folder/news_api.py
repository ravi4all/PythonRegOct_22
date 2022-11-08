import urllib.request as url
import json
# json - javascript object notation

# path = "https://newsapi.org/v2/everything?q=tesla&from=2022-10-08&sortBy=publishedAt&apiKey=695e07af402f4b119f0703e9b19f4683"
# response = url.urlopen(path)

# data = json.load(response)
# print(data["totalResults"])

path = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=695e07af402f4b119f0703e9b19f4683"
response = url.urlopen(path)

data = json.load(response)
articles = data["articles"]
for i in range(len(articles)):
    print(articles[i]["title"])
    print("*" * 50)