from tkinter import *
from tkinter import messagebox

from tkinter.ttk import *

from signature import *


# initialization global variable
keys = None
hash = None



window = Tk()

window.title("APP")
window.geometry("500x300")

def creatk():
    print(2)
    global keys
    keys = RSA.generateKey()
    print(keys)
    key = Label(window, text=str(keys))
    key.place(x = 100, y = 100)
    #
    # savekeybutton = Button(window, text="Save", command= savekey)
    # savekeybutton.place(x = 300, y = 150)



def creatkey():
    text2 = Label(window, text="Sinh key: ")
    text2.place(x= 20, y= 20)
    creatkbutton = Button(window, text="Sinh key", command=creatk)
    creatkbutton.place(x = 20, y = 40)
    print(1)

#tạo mục menu
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Sinh khoá',command=creatkey)

menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)


window.mainloop()
