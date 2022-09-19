#메모장
from tkinter import *

window = Tk()
window.title("*제목없음")
window.geometry("640x480")

filename = "test.txt"
def new_file():
    print("새 파일을 생성합니다.")

def open_file():
    with open(filename,"r",encoding="utf8") as test:
        txt.delete("1.0",END)
        txt.insert(END,test.read())
def save_file():
    with open(filename,"w",encoding="utf8") as test:
        test.write(txt.get("1.0",END))   

menu = Menu(window)
#파일
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="새로 만들기(N)",command=new_file)
menu_file.add_command(label="새 창(W)")
menu_file.add_command(label="열기(O)...",command=open_file)
menu_file.add_command(label="저장(S)",command=save_file)
menu_file.add_command(label="다른 이름으로 저장(A)...")
menu_file.add_separator()
menu_file.add_command(label="페이지 설정(U)...")
menu_file.add_command(label="인쇄(P)...")
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)",command=quit)

#편집
menu_edit = Menu(menu,tearoff=0)
menu_edit.add_command(label="실행 취소(U)",state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="잘라내기(T)",state="disable")
menu_edit.add_command(label="복사(C)",state="disable")
menu_edit.add_command(label="붙여넣기(P)")

#서식
menu_doc = Menu(menu,tearoff=0)
menu_doc.add_checkbutton(label="자동 줄 바꿈(W)")
menu_doc.add_command(label="글꼴(F)...")

#보기
menu_view = Menu(menu,tearoff=0)
menu_view.add_radiobutton(label="확대(I)")
menu_view.add_radiobutton(label="축소(O))")


menu.add_cascade(label="파일(F)",menu=menu_file)
menu.add_cascade(label="편집(E)",menu=menu_edit)
menu.add_cascade(label="서식(O)",menu=menu_doc)
menu.add_cascade(label="보기(V)",menu=menu_view)
menu.add_cascade(label="도움말(H)")

scrollbar = Scrollbar(window)
scrollbar.pack(side="right",fill="y")

txt = Text(window,yscrollcommand=scrollbar.set)
txt.pack(fill="both",expand=True,side="left")
scrollbar.config(command=txt.yview)

window.config(menu=menu)
window.mainloop()