# 대화 상자
from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry("1064x600")

label1 = Label(window, text="입력된 값")
label1.pack()

#value = askinteger("숫자입력", "숫자 1~6을 입력하세요",minvalue=1, maxvalue=6)
#label1.configure(text=str(value))
value1 = askstring("입력", "아무말이나 씨부려주세요")
label1.configure(text=value1)

window.mainloop()