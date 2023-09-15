"""

import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.configure(bg="#DEB887")
window.minsize(width=500,height=500)

def click_button():
    user_entry_input = my_entry.get()
    user_text_input = my_text.get("1.0",tkinter.END)
    if user_entry_input != "":
        print(user_entry_input)
    else:
        pass
    if user_text_input != "":
        print(user_text_input)
    else:
        pass
#label
my_label = tkinter.Label(text="This is a Label", font=("Times New Roman",30, "italic"), bg="#DEB887", fg="#5F9EA0",padx=30,pady=30)
my_label.pack()
#my_label.grid(row=2,column=1)

#button
my_button = tkinter.Button(text="button", command=click_button)

my_button.place(x=250-23.5,y=75)
my_button.update()
#print(my_button.winfo_width())
#print(my_button.winfo_height())
#my_button.grid(row=0,column=1)

#entry
my_entry = tkinter.Entry(width=20)
my_entry.pack()
#my_entry.grid(row=2,column=1)

#text
my_text = tkinter.Text(width=20,height=10)
my_text.pack()
my_text.focus()

#scale
def scale_selected(value):
    print(value)
my_scale = tkinter.Scale(from_=0,to=50, command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())

my_spinbox= tkinter.Spinbox(from_=0,to=50,command=spinbox_selected)
my_spinbox.pack()

#check button
def check_button_selected():
    print(check_state.get())

check_state = tkinter.IntVar()
my_check_button= tkinter.Checkbutton(text="check",variable=check_state, command=check_button_selected)
my_check_button.pack()

#radio button
def radio_selected():
    print(radio_check_state.get())

radio_check_state = tkinter.IntVar()
my_radiobutton = tkinter.Radiobutton(text="first option",value=10,variable=radio_check_state,command=radio_selected)
my_radiobutton_2= tkinter.Radiobutton(text="second option",value=20,variable=radio_check_state,command=radio_selected)

my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = tkinter.Listbox()
my_listbox.configure(width=10, height=5)
name_list = ["İbrahim", "Diyar", "Oskan"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind("<<ListboxSelect>>",listbox_selected)
my_listbox.pack()

window.mainloop()
"""
"""
import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.configure(bg="#DEB887")
window.minsize(width=500,height=500)

#label_1
my_label1 = tkinter.Label(text="Enter your height(cm) ", font=("Times New Roman", 10, "italic"), bg="#DEB887", fg="#800000", padx=5, pady=5)
my_label1.pack()


#entry_1
my_entry1 = tkinter.Entry(width=10, font=("Times New Roman", 10, "italic"), bg="#FFEBCD")
my_entry1.pack()

#label_2
my_label2 = tkinter.Label(text="Enter your weight(kg) ", font=("Times New Roman", 10, "italic"), bg="#DEB887", fg="#800000", padx=5, pady=5)
my_label2.pack()

#entry_2
my_entry2 = tkinter.Entry(width=10, font=("Times New Roman", 10, "italic"), bg="#FFEBCD")
my_entry2.pack()
#label_x
my_labelx = tkinter.Label(text=" ", font=("Times New Roman", 1, "italic"), bg="#DEB887", fg="#800000", padx=5, pady=5)
my_labelx.pack()

def click_button():
    user_entry1 = my_entry1.get()
    user_entry2 = my_entry2.get()
    if user_entry1 =="" or user_entry2 == "":
        my_label3.configure(text="Fill in both blanks")

    else:
        try:
            bmi=float(user_entry2) / ((float(user_entry1) / 100) ** 2)
            if bmi <18.5:
                karşılık = "tiny"
            if 18.5 <bmi<24.9:
                karşılık = "normal weight"
            if 25<bmi<29.9:
                karşılık = "fat"
            if 30<bmi :
                karşılık = "obese"
            my_label3.configure(text="Your BMI is {}.You are {}.".format(bmi, karşılık),)
        except:
            my_label3.configure(text="give me a number !")

#button
my_button = tkinter.Button(text="Calculate", command=click_button,font=("Times New Roman",8, "italic"), bg="#FFEBCD", fg="#800000")

my_button.pack()

#label_3
my_label3 = tkinter.Label(text="Fill the blanks to calculate your BMI value", font=("Times New Roman", 8, "italic"), bg="#DEB887", fg="#800000", padx=5, pady=5)
my_label3.pack()


window.mainloop()
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import base64
import os


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#save notes
def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0",END)
    master_secret = master_secret_input.get()

    if title == "" or message == "" or master_secret == "":
            messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        message_encrypted = encode(master_secret, message)

        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        finally:
            title_entry.delete(0, END)
            master_secret_input.delete(0, END)
            input_text.delete("1.0",END)

#decrypt notes

def decrypt_notes():
    message_encrypted = input_text.get("1.0", END)
    master_secret = master_secret_input.get()

    if message_encrypted == "" or master_secret == "":
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")

#UI

window = Tk()
window.title("Secret File")
window.configure(bg="#DEB887")
window.minsize(width=300,height=500)

img = Image.open("output.png")
resize_image = img.resize((100,100))
img = ImageTk.PhotoImage(resize_image)

panel =Label(window, image = img,bg="#DEB887",fg="#DEB887",)
panel.pack()

title_info_label = Label(text="Enter your title",font=("Times New Roman", 8, "bold"), bg="#DEB887", fg="#800000", padx=5, pady=5)
title_info_label.pack()

title_entry = Entry(width=20 , bg="#FFDEAD",font=("Times New Roman", 8, "italic"), fg="#800000")
title_entry.pack()

input_info_label = Label(text="Enter your secret",font=("Times New Roman", 8, "bold"), bg="#DEB887", fg="#800000", padx=5, pady=5)
input_info_label.pack()

input_text = Text(width=25, height=15,font=("Times New Roman", 8, "normal"),bg="#FFDEAD",fg="#800000")
input_text.pack()

master_secret_label = Label(text="Enter master key",font=("Times New Roman", 8, "bold"), bg="#DEB887", fg="#800000", padx=5, pady=5)
master_secret_label.pack()

master_secret_input = Entry(width=30,font=("Times New Roman", 8, "normal"),bg="#FFDEAD",fg="#800000")
master_secret_input.pack()

save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes,font=("Times New Roman", 8, "bold"),bg="#DEB887", fg="#800000")
save_button.pack()

decrypt_button = Button(text="Decrypt",command=decrypt_notes,font=("Times New Roman", 8, "bold"),bg="#DEB887", fg="#800000")
decrypt_button.pack()
window.mainloop()