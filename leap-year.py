from tkinter import *
import tkinter.messagebox as mb

def leap_year():
    try:
        year = int(txt.get())
    except:
        mb.showinfo('エラー', '整数で入力して下さい')
        return
    T = 'うるう年です'
    F = 'うるう年ではありません'
    if year <= 0:
        mb.showinfo('エラー', '1以上の整数で入力して下さい')
        return
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                ret = T
            else: ret = F
        else: ret = T
    else: ret = F
    mb.showinfo('結果', '{}年は{}'.format(year, ret))

root = Tk()
root.title('うるう年判定')
root .geometry('470x200')

lbl = Label(text='入力された年がうるう年であるかどうかを判定します\n西暦を入力して下さい')
lbl.place(x=65, y=30)

lbl2 = Label(text='年')
lbl2.place(x=310, y=90)

txt = Entry(width=20)
txt.place(x=140, y=90)

btn = Button(text='判定する', height=2, command=leap_year)
btn.pack(fill='x', side='bottom')

root.mainloop()
