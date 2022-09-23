import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a)
print(soup.a.attrs)