from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#generating a password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)#this copy your password to clipboard



def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    errormsg="OOPS"


    if len(website) == 0 or len(password) ==0 :
        messagebox.showinfo(title=errormsg, message="your email or password are not insered, check em!")
    else:

        condition_of_adding_data = messagebox.askokcancel(title=website,
                                                          message=f"these are the informations you tapped : \n Email : {email} "
                                                                  f"\n Password : {password}\n Do you want to save ?")
        if condition_of_adding_data:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} / {email} / {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)





window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

website_label = Label(text="website name", fg="black", bg="white",width=36)
website_label.grid(row=1,column=0)

website_entry = Entry(width=41 )
website_entry.grid(row=1,column=1,columnspan=2)

email_label = Label(text="Email/Username", fg="black", bg="white",width=36)
email_label.grid(row=2,column=0)

email_entry = Entry(width=41 )
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.focus()
email_entry.insert(0,"hichameloualji.example@gmail.com")


password_label = Label(text="Password", fg="black", bg="white",width=36)
password_label.grid(row=3,column=0)

password_entry=Entry(width=23)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

accept_button= Button(text="Use Password",width=40,command=save)
accept_button.grid(row=4,column=1,columnspan=2)


window.mainloop()