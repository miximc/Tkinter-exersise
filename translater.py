# 3. Программа спрашивает пользователя слово и ожидает перевод
#    С тем же интерфейсом должно быть возможно добавлять слова в словарь
import random
import tkinter
words = {
    'hello': 'привет',
    'bye': 'пока',
    'name': 'имя',
    'family': 'семья'
}
rand = random.choice(list(words))
lbl_1 = []
pole = []
print(rand)
def translete():
    global lbl_1
    word = ent_word.get().lower()
    print(word)
    if word == words[rand]:
        tr_lbl = tkinter.Label(window, text='Правильный перевод!')
        tr_lbl.grid(column=0, row=6)
        lbl_1.append(tr_lbl)
    else:
        tr_lbl = tkinter.Label(window, text='Перевод неправильный!')
        tr_lbl.grid(column=0, row=6)
        lbl_1.append(tr_lbl)

def clear_lbl():
    global rand
    ent_word.delete(0, tkinter.END)
    rand = random.choice(list(words))
    for lbl in lbl_1:
        lbl.destroy()

    main_lbl = tkinter.Label(window, text='Как переводится слово "%s" ?' % rand)
    main_lbl.grid(column=0, row=1)

def clear_lbl_1():
    ent_word.delete(0, tkinter.END)
    for lbl in lbl_1:
        lbl.destroy()

window = tkinter.Tk()
window.title('Переводчик')

main_lbl = tkinter.Label(window, text='Как переводится слово "%s"?' % rand)
main_lbl.grid(column=0, row= 1)

ent_word = tkinter.Entry(window, width=16)
ent_word.grid(column=0, row=2)

tr_btn = tkinter.Button(window,text='Перевод', command=translete, width=13)
tr_btn.grid(column=0, row=3)

restart = tkinter.Button(window, text='Новое слово', command=clear_lbl, width=13)
restart.grid(column=0, row=5)

restart_2 = tkinter.Button(window, text='Новая попытка', command=clear_lbl_1, width=13)
restart_2.grid(column=0, row=4)

def new_words(): # РАСШИРЕНИЕ СЛОВАРЯ
    key_new_w = new_word.get()
    trans_new_w = new_word_2.get()
    words[key_new_w] = trans_new_w
    new_butt = tkinter.Button(window, text='Очистить поля',width=16,command=clear_pole_new_dict)
    new_butt.grid(column=2,row=4)
    tr_lbl = tkinter.Label(window, text='Загружено в словарь!')
    tr_lbl.grid(column=2, row=5)
    pole.append(tr_lbl)

def clear_pole_new_dict():
    for lbl in pole:
        lbl.destroy()
    new_word.delete(0, tkinter.END)
    new_word_2.delete(0, tkinter.END)


add_word = tkinter.Label(window, text='Новое английское слово')
add_word.grid(column=1, row=1)

new_word = tkinter.Entry(window, width=19)
new_word.grid(column=2, row=1)

add_word_2 = tkinter.Label(window, text='Перевод английского слова')
add_word_2.grid(column=1, row=2)

new_word_2 = tkinter.Entry(window, width=19)
new_word_2.grid(column=2, row=2)

btn_add_word = tkinter.Button(window, text='Загрузить в словарь', command=new_words)
btn_add_word.grid(column=2, row=3)

window.mainloop()