from tkinter import *

window = Tk()
window.title("계산기")

entry_box = Entry(window,width=30,borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4)

btn7 = Button(window,text="7",padx=25,pady=15)
btn8 = Button(window,text="8",padx=25,pady=15)
btn9 = Button(window,text="9",padx=25,pady=15)
btnx = Button(window,text="*",padx=25,pady=15)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btnx.grid(row=1,column=3)

btn4 = Button(window,text="4",padx=25,pady=15)
btn5 = Button(window,text="5",padx=25,pady=15)
btn6 = Button(window,text="6",padx=25,pady=15)
btnm = Button(window,text="-",padx=25,pady=15)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnm.grid(row=2,column=3)

btn1 = Button(window,text="1",padx=25,pady=15)
btn2 = Button(window,text="2",padx=25,pady=15)
btn3 = Button(window,text="3",padx=25,pady=15)
btnp = Button(window,text="+",padx=25,pady=15)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnp.grid(row=3,column=3)

btn0 = Button(window,text="0",padx=25,pady=15)
btnc = Button(window,text="C",padx=25,pady=15)
btne = Button(window,text="=",padx=25,pady=15)
btns = Button(window,text="/",padx=25,pady=15)

btn0.grid(row=4,column=0)
btnc.grid(row=4,column=1)
btne.grid(row=4,column=2)
btns.grid(row=4,column=3)

window.mainloop()