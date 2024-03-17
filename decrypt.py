import pyAesCrypt
import os
import tkinter
from tkinter import filedialog
from tkinter import *






# функция дешифрования файла
def decryption(file, password):

    #задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод дешифрования
    pyAesCrypt.decryptFile(
                str(file),
                str(os.path.splitext(file)[0]),
                password,
                buffer_size
    )
    # удаляем исходный файл
    os.remove(file)


# функция сканирования директорий
def walking_by_dirs(dir, password):

    #еребираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

def btn1():
    path = tkinter.filedialog.askdirectory()
    file = open('dir2.txt', 'w')
    file.write(path)
    file.close




root = Tk()



root['bg'] = '#000000'
root.title('Дешифратор')
root.geometry('425x125')
root.resizable(width=True, height=True)
root.iconbitmap('icon.ico')
canvas = Canvas(root, height=500, width=500)
frame = Frame(root, bg='white')
title = Label(root, text='Введите пароль:', bd=5, width=15, height=1, bg="white").grid(row=0, column=0)

# создание поля для ввода пароля
passField = tkinter.Entry(root, width=40, bg='white')
passField.grid(row=0, column=1, columnspan=2,rowspan=2)
def clicked():
    password=passField.get()
    return password

# создание кнопки для выбора директории
tkinter.Button(text='Выбрать папку для дешифровки', bd=5, width=30, height=1, font=1, command=lambda: btn1()).grid(row=2,rowspan=2, column=1, columnspan=2)

# создание кнопки для дешифрования файлов
f = open('dir2.txt', 'r')
tkinter.Button(text='Дешифровать файлы', bd=5, width=20, height=1, font=1, command=lambda: walking_by_dirs(*f, clicked())).grid(row=4, column=1, columnspan=2)


root.mainloop()