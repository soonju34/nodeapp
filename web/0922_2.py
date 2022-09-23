import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\DCU\Desktop\pythonapp\업체별 현재시세.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb['업체별 현재시세']

codes = ['035720','035420','005930','000660','066570','005380']

row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(price)
    #엑셀 데이터 입력
    ws[f'B{row}'] = int(price)
    row = row + 1

wb.save(fpath)    