from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# чтобы испл его нужно перед каждым элементом поставить ttk.Button/ttk.Entry
from tkinter import ttk  # используется для оформления элементов в стиле своей системы (windows/linux)
import os, sys
from datetime import datetime

root = Tk()
root.geometry('500x300+400+100')
root.title("PhotoShort")

style_for = ttk.Style()
style_for.configure('my_ttButton', font=("Helvetica", 14))


def folder_path():
    try:
        folder = filedialog.askdirectory(title='Выбирите файл', )
        # выводим текст на Entry, идекс указ без ковычек.
        write_location.delete(0, END)
        write_location.insert(0, folder)
    except Exception:
        pass


def image_sort():
    images_way = write_location.get()
    if images_way:
        print(images_way)
        # проходим по всем папкам и нполучаем то, что ищем
        for folder, subfolder, files in os.walk(images_way):
            for file in files:
                path = os.path.join(folder, file) # получение полного пути к файлам
                # получение время модификадии (показ в секундах)
                mtime = os.path.getmtime(path)
                #  приобразуем эти секунд в норм время
                date= datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d')
                #  Присоединяем к начальному пути, нашу Здравствуйте
                date_folder = os.path.join(images_way,date)
                # Проверяем есть ли такая папка, если нет, то создаём
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                # Перемещяем если такая папка уже есть
                os.renames(path,os.path.join(date_folder, file))
        messagebox.showinfo('Successfully','Сортировка закончена!')
        write_location.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Упс..., кажется эта папка пуста :(')
Label(root,
      text="Здравствуйте.\n Введите место положения папки,\n которую нужно отсортировать\n или впишите в ручную и нажмите 'Начать сортировать'!",
      font=("Courier New", 10), bg='#56ADFF').pack(fill=X)
frame = Frame(root, bg='#0000ff', bd=4)
frame.pack(pady=10, padx=10, fill=X)

write_location = Entry(frame, )
write_location.pack(side=LEFT, expand=1, ipady=2, fill=X)

found_loc = Button(frame, text="Выбрать папку", command=folder_path)
found_loc.pack(side=RIGHT, padx=5)

Button(root, font=("Courier New", 12), text="Начать сортировать", command=image_sort, ).pack(padx=10, fill=X)

frame.mainloop()
