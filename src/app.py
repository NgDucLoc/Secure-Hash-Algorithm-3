from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from tkinter.ttk import *

from signature import *
import re

# initialization global variable
keys = None
hash = None
signed_message = None
cyphertext = None


window = Tk()

window.title("APP")
window.geometry("600x400")

def creatk():
    global keys
    keys = RSA.generateKey()
    print(keys)
    publickey = Label(CreatKey, text="Public Key: " + str(keys[0]))
    publickey.place(x = 100, y = 100)

    privatekey = Label(CreatKey, text="Private Key: " + str(keys[1]))
    privatekey.place(x = 100, y = 120)

    savekeybutton = Button(CreatKey, text="Save", command= savekey)
    savekeybutton.place(x = 300, y = 150)

def savekey():
    global keys
    a = keys
    with open("D:\Git_desktop\Secure-Hash-Algorithm-3\keys.txt", 'w') as f:
        f.write(str(a))
    f.close()

    messagebox.showinfo('Save Key', 'Successfully!')


def importkey():
    global keys
    with open("D:\Git_desktop\Secure-Hash-Algorithm-3\keys.txt", 'r') as f:
        a = f.read()
    f.close()
    a = [int(i) for i in re.findall(r'\d+', a)]
    keys = [[a[0],a[1]],[a[2],a[3]]]
    messagebox.showinfo('Import Key', 'Successfully!')


def saveEC():
    global signed_message
    print(signed_message)
    with open("D:\Git_desktop\Secure-Hash-Algorithm-3\encryption.txt", 'w') as f:
        f.write(signed_message)
    f.close()
    messagebox.showinfo('Save', 'Successfully!')
def importEncryptext():
    global cyphertext
    with open("D:\Git_desktop\Secure-Hash-Algorithm-3\encryption.txt", 'r') as f:
        line = f.readline()
        cyphertext = ''
        while line:
            # if (line != '\n'):
            cyphertext =cyphertext + line
            line = f.readline()
    f.close()
    messagebox.showinfo('Import Encryptext', 'Successfully!')

def creatkey():
    text2 = Label(CreatKey, text="Sinh key: ")
    text2.place(x= 20, y= 20)
    creatkbutton = Button(CreatKey, text="Sinh key", command = creatk)
    creatkbutton.place(x = 20, y = 40)


def encryption():
    encryptext = Label(Encryption, text = "Mã hoá:")
    encryptext.place(x=20, y= 20)
    importKeybutton = Button(Encryption, text = "import Key", command = importkey)
    importKeybutton.place(x= 20, y=40)

    plaintext = Label(Encryption, text = "Nhập bản rõ: ")
    plaintext.place(x=20, y = 80)

    txtinput = Entry(Encryption, width=100)
    txtinput.pack(fill=X, padx=20, pady=100)

    def encrypsub():
        global keys
        message = txtinput.get()
        signa = Signature("SHA3-256")
        global signed_message
        signed_message = signa.sign(message, keys[1])
        print(keys[1])
        cyphertext1 = Label(Encryption, text="Bản mã là:")
        cyphertext1.place(x=20, y=200)

        cyphertext2 = Label(Encryption, text=signed_message)
        cyphertext2.place(x=20, y=230)

        saveECbutton = Button(Encryption, text = "Save", command = saveEC)
        saveECbutton.place(x= 300, y = 270)

    encrypbutton = Button(Encryption, text = "Mã hoá", command= encrypsub)
    encrypbutton.place(x= 300, y = 150)




def verify():
    decryptext = Label(Verify, text="Xác minh:")
    decryptext.place(x=20, y=20)
    importKeybutton = Button(Verify, text="import Key", command=importkey)
    importKeybutton.place(x=20, y=40)

    cyphertext = Button(Verify, text = "import EncrypText", command= importEncryptext)
    cyphertext.place(x=20, y=80)

    def verifysub():
        global keys
        global cyphertext
        signa = Signature("SHA3-256")
        print("cyphertext",cyphertext)
        print(keys[0])
        verify = signa.verifySignedDocument(cyphertext, keys[0])

        result1 = Label(Verify, text = "Kết quả xác minh: "+ str(verify))
        result1.place(x=20, y= 200)

    encrypbutton = Button(Verify, text="Xác minh", command=verifysub)
    encrypbutton.place(x=20, y=150)


def exit():
    window.destroy()

#tao tab
tab_control = ttk.Notebook(window)

CreatKey = ttk.Frame(tab_control)
Encryption = ttk.Frame(tab_control)
Verify = ttk.Frame(tab_control)

tab_control.add(CreatKey, text='CreatKey')
tab_control.add(Encryption, text='Encryption')
tab_control.add(Verify, text='Verify')

creatkey()
encryption()
verify()

tab_control.pack(expand=1, fill='both')

window.mainloop()

