import tkinter.messagebox as msgbox
from tkinter import *

window = Tk()
window.title("제목없음")
window.geometry("640x480")

def info():
    msgbox.showinfo("알림","정상적으로 등록이 되었습니다.")
def warn():
    msgbox.showwarning("경고","등록된 파일의 용량이 초과되었습니다.")
def error():
    msgbox.showerror("에러","접속에러가 발생하였습니다.")   
def okcancel():
    msgbox.askokcancel("확인/취소","png확장자만 등록할 수 있습니다.") 
def retrycancel():
    msgbox.askretrycancel("재시도/취소","등록이 되지 않았습니다.다시 시도하시겠습니까?")
def yesno():
    msgbox.askyesno("예/아니오","파일이 첨부되었습니다. 등록완료하시겠습니까?")           
Button(window,command=info,text="알림").pack()
Button(window,command=warn,text="경고").pack()
Button(window,command=error,text="에러").pack()
Button(window,command=okcancel,text="확인/취소").pack()
Button(window,command=retrycancel,text="재시도/취소").pack()
Button(window,command=yesno,text="예/아니오").pack()
window.mainloop()