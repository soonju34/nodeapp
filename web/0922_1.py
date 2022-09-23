import openpyxl
#엑셀파일 수정
fpath = r'C:\Users\DCU\Desktop\pythonapp\업체별 현재시세.xlsx'

#엑셀 불러오기
wb = openpyxl.load_workbook(fpath)
#시트 선택
ws = wb['업체별 현재시세']

ws['A7'] = '현대차'

wb.save(fpath)
