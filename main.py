import pyAesCrypt
import os
import tkinter
from tkinter import filedialog
from tkinter import *






# функция шифрования файла
def encryption(file, password):

    #задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
                str(file),
                str(file) + ".crp",
                password,
                buffer_size
    )


    # удаляем исходный файл
    os.remove(file)


# функция сканирования директорий
def walking_by_dirs(dir, password):

    #перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

def btn1():
    path = tkinter.filedialog.askdirectory()
    file = open('dir.txt', 'w')
    file.write(path)
    file.close



# создание визуального оформления приложения
root = Tk()
root['bg'] = '#000000'
root.title('Шифратор')
root.geometry('425x125')
root.iconbitmap('icon.ico')
root.resizable(width=True, height=True)
canvas = Canvas(root, height=500, width=500)
frame = Frame(root, bg='black')
title = Label(root, text='Введите пароль:', bd=5, width=15, height=1, bg="white").grid(row=0, column=0)

# создание поля для ввода пароля
passField = tkinter.Entry(root, width=40, bg='white')
passField.grid(row=0, column=1, columnspan=2,rowspan=2)
def clicked():
    password=passField.get()
    return password

# создание кнопки для выбора директории
tkinter.Button(text='Выбрать папку для шифровки', bd=5, width=30, height=1, font=1, command=lambda: btn1()).grid(row=2,rowspan=2, column=1, columnspan=2)

# создание кнопки для шифрования файлов
f = open('dir.txt', 'r')
tkinter.Button(text='Зашифровать файлы', bd=5, width=20, height=1, font=1, command=lambda: walking_by_dirs(*f, clicked())).grid(row=4, column=1, columnspan=2)


root.mainloop()