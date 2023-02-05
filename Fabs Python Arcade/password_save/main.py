from tkinter import *
from tkinter import messagebox
import pyperclip


def password_saver_main():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]

    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password_list}")

    """ password = ""
    for char in password_list:
    password += char """

    print(f"Your password is: {password}")

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def save_password():
        website = entry_website.get()
        mail = entry_email_user.get()
        pw = entry_password.get()
        
        full_entry = f"\n{website} | {mail} | {pw}"

        if (len(website) > 0) and (len(mail) > 0) and (len(pw) > 0):
            is_ok = messagebox.askokcancel(title=website, message=f"These are you credentials you entered: {full_entry}")
        
            if is_ok:
                with open("password_save/data.txt", "a") as file:
                    file.write(full_entry)
                    print("SAVED")

                entry_website.delete(0, "end")
                #entry_email_user.delete(0, "end")
                entry_password.delete(0, "end")
        else:
            messagebox.showerror(title="Invalid Input", message="Fill out the input boxes to save")

    # ---------------------------- UI SETUP ------------------------------- #



    window = Tk()
    window.title("Password Manager")
    window.config(padx= 50, pady= 50)

    new_canvas = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="password_save/logo.png")
    new_canvas.create_image(100, 100, image=logo_img)
    new_canvas.grid(row=0, column=1)

    label_wesite = Label(text="Website")
    label_wesite.grid(row=1, column=0)

    label_wesite = Label(text="Email/Username")
    label_wesite.grid(row=2, column=0)

    label_wesite = Label(text="Password")
    label_wesite.grid(row=3, column=0)

    entry_website = Entry(width=35)
    entry_website.grid(row=1, column=1, columnspan=2)
    entry_website.focus()

    entry_email_user = Entry(width=35)
    entry_email_user.grid(row=2, column=1, columnspan=2)
    entry_email_user.insert(0, "fabsmail@gmail.de")

    entry_password = Entry(width=35)
    entry_password.grid(row=3, column=1)

    add_button = Button(text="Add", width=36, command=save_password)
    add_button.grid(row=4, column=1)

    def file_pw():
        entry_password.insert(0, password)
        pyperclip.copy(password)

    gen_pw_button = Button(text="Generate Password", command=file_pw)
    gen_pw_button.grid(row=3, column=3)


    window.mainloop()