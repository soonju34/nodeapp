import requests
from bs4 import BeautifulSoup

with open("webtoon. txt", "w", encoding="utf8") as web:
    pageNum = 1
    for i in range(1,5):
        print(f"\n\n {pageNum}페이지입니다 \n\n")
        url = "https://comic.naver.com/webtoon/list?titleId=318995&weekday=fri&page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")

        webtoons = soup.find_all("td", attrs={"class" : "title"})
    
        for webtoon in webtoons:
            title = webtoon.a.get_text()
            link = "https://comic.naver.com" +  webtoon.a["href"]
            web.write(title,"(" + link + ")" + '\n')
            print(title, link)
        pageNum = pageNum + 1


webtoon.txt


# webtoons = soup.find_all("div", attrs={"class" : "rating_type"})
# total_rates = 0
# for webtoon in webtoons:
#     rate = webtoon.find("srong").get_text()
#     print(rate)
#     total_rates += float(rate)
#     print(total_rates)

# print(total_rates / len(webtoons))


