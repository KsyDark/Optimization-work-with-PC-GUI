#цвет кнопок
try:
    with open("button.ini", "r") as f:
        yyy = f.read()
        str(yyy)
except:
    yyy = '#ffffff'

#цвет фона
try:
    with open("bg.ini", "r") as f:
        byyy = f.read()
        str(byyy)
except:
    byyy = 'gray22'

from tkinter import *
import os
import sys
from datetime import date, time, datetime
from webbrowser import open
from time import sleep
from bs4 import BeautifulSoup
import requests as req
from tkinter import messagebox
from uuid import uuid4
from pyperclip import copy
import Sport

os.startfile('MinimizeToTray.exe')

#Создаём окно
root = Tk()
root.title("Optimization work with PC GUI - ver 5.6")
width = root.resizable(width=False, height=False)
root.geometry('800x600')
root["bg"] = "gray22"

#Условие на случай, если пропадёт иконка
try:
    root.iconbitmap(r'О.Р.ПК.ico')
except:
    pass

#Условие, если пропадёт картинка фона
try:
    C = Canvas(root, height=800, width=600)
    filename = PhotoImage(file =byyy)
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
except:
    pass

#Модуль напоминаний
def koef():
    today = date.today()
    v = int(today.weekday())
    if v == 0:
        #Понедельник
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

    elif v == 1:
        #Вторник
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

    elif v == 2:
        #Среда
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

    elif v == 3:
        #Четверг
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

    elif v == 4:
        #Пятница
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

    elif v == 5:
        #Суббота
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

    elif v == 6:
        #Воскресенье
        def reference():
            messagebox.showinfo("Справка","Ваш текст")
        
        button9=Button(root, text='Справка', fg="black", font="Atial 12", command = reference, bg=yyy)
        button9.pack()
        button9.place(relx=0.82, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

koef()

#Коронавирус - Россия
def koef0():
    try:
        resp = req.get("https://yandex.ru/maps/covid19?ll=58.510520%2C41.006260&z=3")
        soup = BeautifulSoup(resp.text, 'lxml')
        kor = soup.find("div", {"class": "covid-stat-view__item-value"}).text.strip()

        lable0=Label(root, text='Коронавирус - Россия - ' + kor, fg="black", font="Atial 14", bg=yyy)
        lable0.pack()
        lable0.place(relx=0.0119, rely=0.79)
    except:
        lable0=Label(root, text='Подключите интернет для отображения статистики', fg="black", font="Atial 14", bg=yyy)
        lable0.pack()
        lable0.place(relx=0.0119, rely=0.79)
        
koef0()

#Выход
def koef1(event):
    sys.exit()

button1=Button(root, text='Выход', fg="black", font="Atial 12", bg=yyy)
button1.bind("<Button>", koef1)
button1.place(relx=0.1, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)


#Лог версий
def koef2(event):
    pass

button2=Button(root, text='Лог версий', fg="black", font="Atial 12", bg=yyy)
button2.bind("<Button>", koef2)
button2.place(relx=0.28, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

#Study
def koef3(event):
    root1 = Tk()
    root1.title("Study")
    root1.resizable(width=False, height=False)
    root1.geometry('280x130')
    #Python
    def koef9(event):
        #Вконтакте
        open("https://vk.com/id633731535")
        #Как скомпилировать python приложение?
        open("http://toolmark.ru/kak-skompilirovat-python-prilozhenie/")
        #Основы Python
        open("https://www.youtube.com/watch?v=vqsalStEu38&list=PLlWXhlUMyooaeSj8L8tVVbtUo0WCO4ORR&index=17")
        #GitHub
        open("https://github.com/")
        #Checkio
        open("https://checkio.org/")

    button9=Button(root1, text='Python', fg="black", font="Atial 12")
    button9.bind("<Button>", koef9)
    button9.place(height=40, width=140, bordermode=OUTSIDE)
    #SQL
    def koef10(event):
        #SQL Задачи и решения
        open("http://www.sql-tutorial.ru/ru/content.html")
        #Упражнения по SQL
        open("http://www.sql-ex.ru/learn_exercises.php")
        #Гоша Дударь
        open("https://www.youtube.com/watch?v=BfaKBs_eQXw")

    button10=Button(root1, text='SQL', fg="black", font="Atial 12")
    button10.bind("<Button>", koef10)
    button10.place(rely=0.3, height=40, width=140, bordermode=OUTSIDE)
    #HTML
    def koef11(event):
        #Справочник по HTML
        open("http://htmlbook.ru/samhtml")

    button11=Button(root1, text='HTML', fg="black", font="Atial 12")
    button11.bind("<Button>", koef11)
    button11.place(relx=0.5, height=40, width=140, bordermode=OUTSIDE)
    #C#
    def koef12(event):
        #Канал CODE BLOG - Программирование и C#
        open("https://www.youtube.com/user/admshwan/videos")
        #Плейлист C#
        open("https://www.youtube.com/playlist?list=PLIIXgDT0bKw4OmiZ9yGmShKsY0XncViZ8")

    button12=Button(root1, text='C#', fg="black", font="Atial 12")
    button12.bind("<Button>", koef12)
    button12.place(relx=0.5, rely=0.3, height=40, width=140, bordermode=OUTSIDE)
    #English
    def koef13(event):
        #Справочник по грамматике английского языка
        open("https://www.study.ru/handbook")

    button13=Button(root1, text='English', fg="black", font="Atial 12")
    button13.bind("<Button>", koef13)
    button13.place(rely=0.61, height=52, width=280, bordermode=OUTSIDE)
    #Условие на случай, если пропадёт иконка
    try:
        root1.iconbitmap(r'О.Р.ПК.ico')
        root1.mainloop()
    except:
        root1.mainloop()
        pass

button3=Button(root, text='Study', fg="black", font="Atial 12", bg=yyy)
button3.bind("<Button>", koef3)
button3.place(relx=0.46, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

#Развлечения
def koef4(event):
    #Хороший выбор!
    open("https://www.youtube.com/user/GoodChoiceShow/videos")
    #Новинки IT 
    open("https://www.youtube.com/user/MarozOFF/videos")
    #Jennierubyjane Official
    open("https://www.youtube.com/channel/UCNYi_zGmR519r5gYdOKLTjQ")
    #CORE
    open("https://www.youtube.com/user/1servicecore/videos")
    #Лёша Кластер
    open("https://www.youtube.com/user/ClusterMeerkat/videos")
    #Уютный подвальчик
    open("https://www.youtube.com/user/podval4ikshow/videos")
    #Кирилл Лейфер
    open("https://www.youtube.com/user/kogdazjasdohnu/videos")
    #stalkash
    open("https://www.youtube.com/channel/UCOpm7EqPBtznEwYNNZrz1FQ/videos")
    #TEHNOGLOBE TV
    open("https://www.youtube.com/user/bulletproofzzz7o62/videos")
    #Russian Geek
    open("https://www.youtube.com/user/PxlDevil/videos")
    #Pixel_Devil Live
    open("https://www.youtube.com/user/pixeldevillive/videos")
    #hhwang - кто молодец?!
    open("https://www.youtube.com/channel/UCkJhWA2SEYbVYnE2Y2FWryA/videos")
    #Nitroxsenys
    open("https://www.youtube.com/channel/UCF3d6ZcTRBhnrNC0-cvzicw/videos")
    #Odd Tinkering
    open("https://www.youtube.com/channel/UCf_suVrG2dA5BTjJhNLwthQ/videos")
    #Alpha Centauri
    open("https://www.youtube.com/c/AlphaCentauriChannel/videos")
    #Primitive Technology
    open("https://www.youtube.com/channel/UCAL3JXZSzSm8AlZyD3nQdBA/videos")
    #BLACKPINK
    open("https://www.youtube.com/c/BLACKPINKOFFICIAL/videos")
    #Lilifilm Official
    open("https://www.youtube.com/channel/UC35HKvKYPkri4Grd5KXl3wQ/videos")
    #Oleg Kerman
    open("https://www.youtube.com/c/OlegKerman/videos")
    #sinc LAIR
    open("https://www.youtube.com/c/sincLAIRchannel/videos")

button4=Button(root, text='Развлечения', fg="black", font="Atial 12", bg=yyy)
button4.bind("<Button>", koef4)
button4.place(relx=0.64, rely=0.875, anchor="c", height=40, width=140, bordermode=OUTSIDE)

#Мои проекты
def koef5(event):
    root2 = Tk()
    root2.title("Мои проекты")
    root2.resizable(width=False, height=False)
    root2.geometry('500x130')
    #Настройка Windows 10
    def koef9(event):
        pass

    button14=Button(root2, text='Свободный слот', fg="black", font="Atial 9")
    button14.bind("<Button>", koef9)
    button14.place(height=40, width=250, bordermode=OUTSIDE)
    #Расширенное меню персонализации
    def koef10(event):
        pass

    button15=Button(root2, text='Свободный слот', fg="black", font="Atial 9")
    button15.bind("<Button>", koef10)
    button15.place(rely=0.3, height=40, width=250, bordermode=OUTSIDE)
    #Общий набор программ
    def koef11(event):
        pass

    button16=Button(root2, text='Свободный слот', fg="black", font="Atial 9")
    button16.bind("<Button>", koef11)
    button16.place(relx=0.5, height=40, width=250, bordermode=OUTSIDE)
    #Активатор Windows 10
    def koef12(event):
        pass

    button17=Button(root2, text='Свободный слот', fg="black", font="Atial 9")
    button17.bind("<Button>", koef12)
    button17.place(relx=0.5, rely=0.3, height=40, width=250, bordermode=OUTSIDE)
    #Свободный слот
    def koef13(event):
        pass

    button18=Button(root2, text='Свободный слот', fg="black", font="Atial 9")
    button18.bind("<Button>", koef13)
    button18.place(rely=0.61, height=52, width=500, bordermode=OUTSIDE)
    #Условие на случай, если пропадёт иконка
    try:
        root2.iconbitmap(r'О.Р.ПК.ico')
        root2.mainloop()
    except:
        root2.mainloop()
        pass

button5=Button(root, text='Мои проекты', fg="black", font="Atial 12", bg=yyy)
button5.bind("<Button>", koef5)
button5.place(relx=0.1, rely=0.95, anchor="c", height=40, width=140, bordermode=OUTSIDE)

#Выключить ПК
def koef6(event):
    os.system('shutdown /s /t 2')
    sys.exit()

button6=Button(root, text='Выключить ПК', fg="black", font="Atial 12", bg=yyy)
button6.bind("<Button>", koef6)
button6.place(relx=0.28, rely=0.95, anchor="c", height=40, width=140, bordermode=OUTSIDE)

#Нужное
def koef7(event):
    root3 = Tk()
    root3.title("Нужное")
    root3.resizable(width=False, height=False)
    root3.geometry('500x130')
    #Пожертвования
    def koef9(event):
        pass

    button18=Button(root3, text='Пожертвования', fg="black", font="Atial 9")
    button18.bind("<Button>", koef9)
    button18.place(height=40, width=250, bordermode=OUTSIDE)
    #Пройденные игры
    def koef10(event):
        pass

    button19=Button(root3, text='Пройденные игры', fg="black", font="Atial 9")
    button19.bind("<Button>", koef10)
    button19.place(rely=0.3, height=40, width=250, bordermode=OUTSIDE)
    #Свободный слот
    def koef11(event):
        pass

    button20=Button(root3, text='Свободный слот', fg="black", font="Atial 9")
    button20.bind("<Button>", koef11)
    button20.place(relx=0.5, height=40, width=250, bordermode=OUTSIDE)
    #Свободный слот
    def koef12(event):
        pass

    button21=Button(root3, text='Свободный слот', fg="black", font="Atial 9")
    button21.bind("<Button>", koef12)
    button21.place(relx=0.5, rely=0.3, height=40, width=250, bordermode=OUTSIDE)
    #Свободный слот
    def koef13(event):
        pass

    button22=Button(root3, text='Свободный слот', fg="black", font="Atial 9")
    button22.bind("<Button>", koef13)
    button22.place(rely=0.61, height=52, width=500, bordermode=OUTSIDE)
    #Условие на случай, если пропадёт иконка
    try:
        root3.iconbitmap(r'О.Р.ПК.ico')
        root3.mainloop()
    except:
        root3.mainloop()
        pass

button7=Button(root, text='Нужное', fg="black", font="Atial 12", bg=yyy)
button7.bind("<Button>", koef7)
button7.place(relx=0.46, rely=0.95, anchor="c", height=40, width=140, bordermode=OUTSIDE)

#Работа
def koef8(event):
    pass

button8=Button(root, text='Работа', fg="black", font="Atial 12", bg=yyy)
button8.bind("<Button>", koef8)
button8.place(relx=0.64, rely=0.95, anchor="c", height=40, width=140, bordermode=OUTSIDE)
#Копировать GUID
def oneuuid(event):
    xxx = str(uuid4())
    copy(xxx)

button23=Button(root, text='Копировать GUID', fg="black", font="Atial 12", bg=yyy)
button23.bind("<Button>", oneuuid)
button23.place(relx=0.82, rely=0.95, anchor="c", height=40, width=140, bordermode=OUTSIDE)
#SQL
def koef14(event):
    pass

button24=Button(root, text='SQL', fg="black", font="Atial 12", bg=yyy)
button24.bind("<Button>", koef14)
button24.place(relx=0.95, rely=0.9114, anchor="c", height=85, width=60, bordermode=OUTSIDE)

root.mainloop()
