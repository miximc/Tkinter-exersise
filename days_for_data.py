# 2. Программа ожидает ввода желаемой даты и выводит количество дней до неё
import tkinter
import datetime
line = 10
lbl_1 = []

def days():
    d_tooday = user_ent.get()
    day = datetime.date(int(d_tooday[0:4]),int(d_tooday[4:6]),int(d_tooday[6:]))
    tooday = datetime.date.today()
    days = (str(day - tooday)).split()
    lbl = tkinter.Label(window, text='Осталось дней: %s' % days[0])
    lbl.grid(column=1,row=4)
    lbl_1.append(lbl)

def clear_lbl():
    user_ent.delete(0, tkinter.END)
    for lbl in lbl_1:
        lbl.destroy()

window = tkinter.Tk()
window.title('Программа для определения количества дней до даты!')
lbl = tkinter.Label(window, text='Введите дату в формате ГГГГММДД:')
lbl.grid(column=1, row=0)

user_ent = tkinter.Entry(window, width=line)
user_ent.grid(column=1, row=1)

btn = tkinter.Button(window, text='Расчитать', command=days, width=line-2)
btn.grid(column=1, row=2)

restart = tkinter.Button(window, text='Стереть', command=clear_lbl, width=line-2)
restart.grid(column=1, row=3)


window.mainloop()
