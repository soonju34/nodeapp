#이미지 프로그래밍
import tkinter.ttk as ttk
from tkinter import *

window = Tk()
window.title("이미지 프로그램")

#파일버튼 프레임
frame1 = Frame(window)
frame1.pack(fill="x",padx=5,pady=5)

btn_add = Button(frame1,text="파일추가",padx=5,pady=5,width=12)
btn_add.pack(side="left")

btn_del = Button(frame1,text="선택삭제",padx=5,pady=5,width=12)
btn_del.pack(side="right")

#파일리스트 프레임
list_frame = Frame(window)
list_frame.pack(fill="both",padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list = Listbox(list_frame,selectmode="extenden",height=15,yscrollcommand=scrollbar.set)
list.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list.yview)

#저장경로 프레임
path_frame = LabelFrame(window, text="저장경로")
path_frame.pack(fill="x",padx=5,pady=5,ipady=5)

path1 = Entry(path_frame)
path1.pack(side="left",fill="x",expand=True,ipady=4,padx=5,pady=5)

btn_path = Button(path_frame,text="찾아보기",width=10)
btn_path.pack(side="right",padx=5,pady=5)

#옵션 프레임
opt_frame = LabelFrame(window,text="옵션")
opt_frame.pack(padx=5,pady=5,ipady=5)

width1 = Label(opt_frame,text="가로넓이",width=8)
width1.pack(side="left",padx=5,pady=5)

opt_width = ["원래 사이즈","1024","800","640","320"]
cmb_width = ttk.Combobox(opt_frame,state="readonly",values=opt_width,width=10)
cmb_width.current(1)
cmb_width.pack(side="left",padx=5,pady=5)

width2 = Label(opt_frame,text="간격",width=8)
width2.pack(side="left",padx=5,pady=5)

opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(opt_frame,state="readonly",values=opt_space,width=10)
cmb_space.current(0)
cmb_space.pack(side="left")

width3 = Label(opt_frame,text="포맷",width=8)
width3.pack(side="left",padx=5,pady=5)

opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(opt_frame,state="readonly",values=opt_format,width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5,pady=5)

#프로그레스바
progress_frame = LabelFrame(window,text="진행상황")
progress_frame.pack(fill="x",padx=5,pady=5,ipady=5)

pvar = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame,maximum=100)
progress_bar.pack(fill="x",padx=5,pady=5)

#실행프레임
play_frame = Frame(window)
play_frame.pack(fill="x",padx=5,pady=5)

btn_stop = Button(play_frame,padx=5,pady=5,text="닫기",width=12,command=window.quit)
btn_stop.pack(side="right",padx=5,pady=5)

btn_start = Button(play_frame,padx=5,pady=5,text="시작",width=12)
btn_start.pack(side="right",padx=5,pady=5)



window.mainloop()