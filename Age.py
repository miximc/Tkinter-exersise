# 1. Программа ожидает ввода даты рождения и ниже пишет возраст

import tkinter
from datetime import datetime
current_datetime = datetime.now()
digits = 10
lbl_1 = []
def age(year, mounth, day):
    current_year = current_datetime.year
    current_mounth = current_datetime.month
    current_day = current_datetime.day
    result = current_year - year
    if mounth > current_mounth:
        result -= 1
    if mounth == current_mounth:
        if day > current_day:
            result -= 1
    elif day > current_day:
        result -= 1
    return result

def next_try(): # Создает очередной Label с попыткой
    result = pole.get()
    lbl = tkinter.Label( # вписывает текст на окно
        window,
        text='Ваш возраст: %i'% age(int(result[:4]),int(result[4:6]),int(result[-1])))
    lbl.grid(column=0, row=5)
    #print(age(int(result[:4]),int(result[4:7]),int(result[-1])))  - проверял принт в интерпретаторе
    lbl_1.append(lbl)
def clear_lbl():
    pole.delete(0, tkinter.END)
    for lbl in lbl_1:
        lbl.destroy()

window = tkinter.Tk()
window.title('Программа для определения возаста!')

user_lbl = tkinter.Label(
    window,
    text='Введите вашу дату рождения в формате ГГГГММДД')
user_lbl.grid(column=0, row=0)

pole = tkinter.Entry(
    window,
    width=digits)
pole.grid(column=0, row=1)

btn_use = tkinter.Button(
    window,
    text='Загрузить',
    command=next_try,
)
btn_use.grid(column=0, row=2)

restart = tkinter.Button(
    window,
    text='Стереть',
    command=clear_lbl,
    width=digits-2
)
restart.grid(column=0, row=4)









window.mainloop()