from tkinter import *

from tkinter.ttk import *

from signature import *


window = Tk()

window.title("APP")


def clicked2():
    keys = RSA.generateKey()
    key = Label(window, text=str(keys))
    key.grid(column=2, row=6)

# reset window
def New():
    window.destroy()

def creatkey():
    text2 = Label(window, text="Sinh key: ")
    text2.grid(column=0, row = 4)
    btn = Button(window, text="Sinh key", command=clicked2)
    btn.grid(column=0, row=5)

def encryption():
    pass

def decryption():
    pass

def exit():
    pass

#tạo mục menu
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New',command=New)
new_item.add_separator()
new_item.add_command(label='Sinh khoá',command=creatkey)
new_item.add_separator()
new_item.add_command(label='Mã hoá',command=encryption)
new_item.add_separator()
new_item.add_command(label='Giải mã',command=decryption)
new_item.add_separator()
new_item.add_command(label='Exit',command=exit)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)





#chọn loại SHA3
# lbl = Label(window, text="Chọn loại SHA3: ")
# lbl.grid(column=0, row=0)
# selected = IntVar()
# rad1 = Radiobutton(window, text='SHA3-224', value=1, variable= selected)
# rad2 = Radiobutton(window, text='SHA3-256', value=2, variable= selected)
# rad3 = Radiobutton(window, text='SHA3-384', value=3, variable= selected)
# rad4 = Radiobutton(window, text='SHA3-512', value=4, variable= selected)
#
# def clicked1():
#     type = selected.get()
#     print(type)
#     if (type ==1):
#         signa = Signature("SHA3-256")
#     elif (type == 2):
#         signa = Signature("SHA3-224")
#     elif (type == 3):
#         signa = Signature("SHA3-384")
#     elif (type == 4):
#         signa = Signature("SHA3-512")
#     return signa
# btn = Button(window, text="Chọn loại", command=clicked1)
# rad1.grid(column=0, row=1)
# rad2.grid(column=1, row=1)
# rad3.grid(column=2, row=1)
# rad4.grid(column=3, row=1)
# btn.grid(column=4, row=1)
#
#
# #Sinh key
# text2 = Label(window, text="Sinh key: ")
# text2.grid(column=0, row = 4)
# def clicked2():
#     keys = RSA.generateKey()
#     key = Label(window, text=str(keys))
#     key.grid(column=2, row=6)

#
# def encryption():
#     btn = Button(window, text="Sinh key", command=clicked2)
#     btn.grid(column=0, row=5)
#
# def decryption():
#     pass
#
#
#
# encryp = Button(window, text="Mã hoá", command=encryption)
# encryp.grid(column=0, row=5)
# decryp = Button(window, text="Giải mã", command=decryption)
# decryp.grid(column=2, row=5)
#
# #nhập message
# txt = Entry(window, width=10)
# txt.grid(column=1, row=1000)

window.mainloop()
