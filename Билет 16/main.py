import tkinter as tk

# Библиотеки обязательные для печати
import win32api
import win32print

# Библиотеки обязательные для Excel
import pandas as pd
import openpyxl



def func1():
    entryData.delete(0, tk.END)
    entryFIO.delete(0, tk.END)
    entryAUD.delete(0, tk.END)
    entryTimeIn.delete(0, tk.END)
    entryTimeOut.delete(0, tk.END)
def func2():
    win32api.ShellExecute(0,"printto","test.txt",'"%s"' % win32print.GetDefaultPrinter(), ".",0)
    print("Напечатано! ну потчи)")

    
def func3():
    df = pd.read_table('test.txt', sep='\t')
    df.to_excel('output.xlsx', 'Sheet1')
    
def func4():
    string = "\n" + entryData.get() + "\t" + entryFIO.get() + "\t" + entryAUD.get() + "\t" + entryTimeIn.get() + "\t" + entryTimeOut.get()
    file = open("test.txt",'a')
    file.write(string)
    


window = tk.Tk()

frame = tk.Frame(
    master=window,
    width=460,
    height=200,
    bg="snow4"
    )
frame.pack()


entryData = tk.Entry(
    master=frame,
    fg="snow",
    bg="snow3",
    width=50
    )
entryFIO = tk.Entry(
    master=frame,
    fg="snow",
    bg="snow3",
    width=50
    )
entryAUD = tk.Entry(
    master=frame,
    fg="snow",
    bg="snow3",
    width=50
    )
entryTimeIn = tk.Entry(
    master=frame,
    fg="snow",
    bg="snow3",
    width=50
    )
entryTimeOut = tk.Entry(
    master=frame,
    fg="snow",
    bg="snow3",
    width=50
    )

labelData = tk.Label(
    master=frame,
    text="Дата:",
    fg="white",
    bg="black"
    )
labelFIO= tk.Label(
    master=frame,
    text="ФИО:",
    fg="white",
    bg="black"
    )
labelAUD = tk.Label(
    master=frame,
    text="Аудитория:",
    fg="white",
    bg="black"
    )
labelTimeIn = tk.Label(
    master=frame,
    text="Время получения:",
    fg="white",
    bg="black"
    )
labelTimeOut = tk.Label(
    master=frame,
    text="Время сдачи:",
    fg="white",
    bg="black"
    )

labelData.place(x=0, y=0)
labelFIO.place(x=0, y=20)
labelAUD.place(x=0, y=40)
labelTimeIn.place(x=0, y=60)
labelTimeOut.place(x=0, y=80)

entryData.place(x=150, y=0)
entryFIO.place(x=150, y=20)
entryAUD.place(x=150, y=40)
entryTimeIn.place(x=150, y=60)
entryTimeOut.place(x=150, y=80)


button1 = tk.Button(
    text= "Очистить",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=func1,
)

button2 = tk.Button(
    text="Отпечатать файл",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=func2,
)

button3 = tk.Button(
    text="Показать в Excel",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=func3,
)

button4 = tk.Button(
    text="Добавить запись",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=func4,
)

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)

window.mainloop()
