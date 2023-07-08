import tkinter.messagebox as messagebox

# pip install customtkinter
import customtkinter

from tkinter import *

import os

from tkinter.ttk import *

from signature import *
import re

# initialization global variable
keys = None
hash = None
signed_message = None
cyphertext = None
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))


def creatk():
    global keys
    keys = RSA.generateKey()
    print(keys)
    publickey = customtkinter.CTkLabel(
        CreatKey, text="Public Key: " + str(keys[0]))
    publickey.grid(row=0, column=0, padx=(
        20, 20), pady=(20, 20), sticky="sw")

    privatekey = customtkinter.CTkLabel(
        CreatKey, text="Private Key: " + str(keys[1]))

    privatekey.grid(row=1, column=0, padx=(
        20, 20), pady=(20, 20), sticky="nw")

    savekeybutton = customtkinter.CTkButton(
        CreatKey, text="Save key", command=savekey, fg_color="transparent", border_width=3, text_color=("gray10", "#DCE4EE"))
    savekeybutton.grid(row=1, column=0, padx=(
        20, 20), pady=(20, 20), sticky="sw")


def savekey():
    global keys
    a = keys
    with open(ROOT_PATH + "\keys.txt", 'w') as f:
        f.write(str(a))
    f.close()

    messagebox.showinfo('Save Key', 'Successfully!')


def importkey():
    global keys
    with open(ROOT_PATH + "\keys.txt", 'r') as f:
        a = f.read()
    f.close()
    a = [int(i) for i in re.findall(r'\d+', a)]
    keys = [[a[0], a[1]], [a[2], a[3]]]
    messagebox.showinfo('Import Key', 'Successfully!')


def saveEC():
    global signed_message
    print(signed_message)
    with open(ROOT_PATH + "\encryption.txt", 'w') as f:
        f.write(signed_message)
    f.close()
    messagebox.showinfo('Save', 'Successfully!')


def importEncryptext():
    global cyphertext
    with open(ROOT_PATH + "\encryption.txt", 'r') as f:
        line = f.readline()
        cyphertext = ''
        while line:
            # if (line != '\n'):
            cyphertext = cyphertext + line
            line = f.readline()
    f.close()
    messagebox.showinfo('Import Encryptext', 'Successfully!')


def creatkey():
    creatkbutton = customtkinter.CTkButton(
        CreatKey, text="Sinh key", command=creatk, fg_color="transparent", border_width=3, text_color=("gray10", "#DCE4EE"))

    creatkbutton.grid(row=0, column=0, padx=(
        20, 20), pady=(20, 20), sticky="nw")


def encryption():
    encryptext = customtkinter.CTkLabel(Encryption, text="Mã hoá:")
    encryptext.place(x=20, y=20)
    importKeybutton = customtkinter.CTkButton(
        Encryption, text="import Key", command=importkey)
    importKeybutton.place(x=20, y=40)

    plaintext = customtkinter.CTkLabel(Encryption, text="Nhập bản rõ: ")
    plaintext.place(x=20, y=80)

    txtinput = customtkinter.CTkEntry(Encryption, width=100)
    txtinput.pack(fill=X, padx=20, pady=100)

    def encrypsub():
        global keys
        message = txtinput.get()
        signa = Signature("SHA3-256")
        global signed_message
        signed_message = signa.sign(message, keys[1])
        print(keys[1])
        cyphertext1 = customtkinter.CTkLabel(Encryption, text="Bản mã là:")
        cyphertext1.place(x=20, y=200)

        # cyphertext2 = customtkinter.CTkLabel(Encryption, text=signed_message)
        textbox = customtkinter.CTkTextbox(Encryption, width=500)
        # cyphertext2grid(row=0, column=1, padx=(
        #     20, 0), pady=(20, 0), sticky="nsew")
        textbox.insert("0.0", signed_message)

        textbox.place(x=20, y=230)
        # cyphertext2.place(x=20, y=230)

        saveECbutton = customtkinter.CTkButton(
            Encryption, text="Save", command=saveEC)
        saveECbutton.place(x=550, y=270)

    encrypbutton = customtkinter.CTkButton(
        Encryption, text="Mã hoá", command=encrypsub)
    encrypbutton.place(x=300, y=150)


def verify():
    decryptext = customtkinter.CTkLabel(Verify, text="Xác minh:")
    decryptext.grid(row=0, column=0, padx=20)

    decryptext.grid(row=0, column=0, padx=20, pady=(20, 10))
    importKeybutton = customtkinter.CTkButton(
        Verify, text="import Key", command=importkey)
    # importKeybutton.place(x=20, y=40)
    importKeybutton.grid(row=1, column=0, padx=20, pady=(20, 10))

    cyphertext = customtkinter.CTkButton(Verify, text="import EncrypText",
                                         command=importEncryptext)
    cyphertext.grid(row=2, column=0, padx=20, pady=(20, 10))

    def verifysub():
        global keys
        global cyphertext
        signa = Signature("SHA3-256")
        print("cyphertext", cyphertext)
        print(keys[0])
        verify = signa.verifySignedDocument(cyphertext, keys[0])

        result1 = customtkinter.CTkLabel(
            Verify, text="Kết quả xác minh: " + str(verify))
        result1.grid(row=4, column=0, padx=20, pady=(20, 10))

    encrypbutton = customtkinter.CTkButton(
        Verify, text="Xác minh", command=verifysub)
    encrypbutton.grid(row=3, column=0, padx=20, pady=(20, 10))


def exit():
    window.destroy()


def open_input_dialog_event():
    dialog = customtkinter.CTkInputDialog(
        text="Type in a number:", title="CTkInputDialog")
    print("CTkInputDialog:", dialog.get_input())


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def create_key_b_event():
    print("sidebar_button click")
    tabview.set('Create Key')


def encrypt_b_event():
    print("sidebar_button click")
    tabview.set('Encrypt')


def verify_b_event():
    print("sidebar_button click")
    tabview.set('Verify')


app = customtkinter.CTk()
app.geometry(f"{1100}x{580}")

# configure window

# configure grid layout (4x4)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

# create sidebar frame with widgets
sidebar_frame = customtkinter.CTkFrame(
    app, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)
logo_label = customtkinter.CTkLabel(
    sidebar_frame, text="App", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

sidebar_button_1 = customtkinter.CTkButton(
    sidebar_frame, text='Create Key', command=create_key_b_event)
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
sidebar_button_2 = customtkinter.CTkButton(
    sidebar_frame, text='Encrypt', command=encrypt_b_event)
sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
sidebar_button_3 = customtkinter.CTkButton(
    sidebar_frame, text='Verify', command=verify_b_event)
sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
appearance_mode_label = customtkinter.CTkLabel(
    sidebar_frame, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Light", "Dark"],
                                                          command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(
    row=6, column=0, padx=20, pady=(10, 10))


# create tabview
tabview = customtkinter.CTkTabview(
    app, width=250, state='disable')
tabview.grid(row=0, column=1, columnspan=3, rowspan=4, sticky="nsew")
tabview.add("Create Key")
tabview.add("Encrypt")
tabview.add("Verify")


tabview.tab("Create Key").grid_columnconfigure(
    0, weight=1)  # configure grid of individual tabs
tabview.tab("Encrypt").grid_columnconfigure(1, weight=1)
tabview.tab("Encrypt").grid_columnconfigure((2, 3), weight=0)
tabview.tab("Encrypt").grid_rowconfigure((0, 1, 2), weight=1)

tabview.tab("Create Key").grid_columnconfigure(1, weight=1)
tabview.tab("Create Key").grid_columnconfigure((2, 3), weight=0)
tabview.tab("Create Key").grid_rowconfigure((0, 1, 2), weight=1)

tabview.tab("Verify").grid_columnconfigure(
    0, weight=1)


CreatKey = tabview.tab("Create Key")
Encryption = tabview.tab("Encrypt")
Verify = tabview.tab("Verify")

creatkey()
encryption()
verify()

app.mainloop()
