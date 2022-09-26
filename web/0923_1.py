import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a)
#print(soup.a.attrs)
#print(soup.a["href"])
#print(soup.find("a", attrs={"class" : "Nbtn_upload"}).get_text())
rank1 = soup.find("li", attrs={"class" : "rank01"})
#print(rank1.a.get_text())
#rank2 = (rank1.next_sibling.next_sibling)   #두번째순위
#print(rank2.a.get_text())
#rank2_1 = rank2.previous_sibling.previous_sibling
#print(rank2_1.a.get_text())
#print(rank1.parent)   #rank01의 부모부터 출력해달라
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank1_1 = rank2.find_previous_sibling("li")

#title = soup.find("a", text="참교육")
#print(title)

titles = soup.find_all("a",attrs={"class" : "title"})
for title in titles:
    print(title.get_text)
