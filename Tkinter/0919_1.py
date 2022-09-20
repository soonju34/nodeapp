# 마우스 이벤트처리
import tkinter.messagebox as msgbox
from tkinter import *

def leftclick(event):
    msgbox.showinfo("마우스 왼쪽을 클릭햇습니다")

def imageClick(event):
    msgbox.showinfo("마우스","이미지파일 클릭")

window = Tk()
window.geometry("1024x768")

photo = PhotoImage(file = "at-g1357f2a6c_640.png")
label1 = Label(window, image=photo)
label1.pack(expand = True, anchor=CENTER) 

label1.bind("<Button>", imageClick)
# Button-1 왼쪽 버튼 Button-2 가운데 버튼 Button-3 오른쪽 버튼 
#window.bind("<Button-1>", leftclick)   
window.mainloop()

