from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pswd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for n in range(randint(2, 4))]
    password_numbers = [choice(numbers) for s in range(randint(2, 4))]

    pswd_lst = password_numbers + password_symbols + password_letters

    shuffle(pswd_lst)
    pd = "".join(pswd_lst)

    psd.insert(0,pd)
    pyperclip.copy(pd)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = webs.get()
    email = em.get()
    password = psd.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                                                              f"\nPassword: {password} \nIs it okay to save? ")

        if len(website) != 0 and len(password) != 0 and is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                webs.delete(0, END)
                psd.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Label
website = Label(text="Website: ", fg= "blue")
website.grid(column=0, row=1)
email = Label(text="Email/Username: ", fg= "blue")
email.grid(column=0, row=2)
pswd = Label(text="Password: ", fg= "blue")
pswd.grid(column=0, row=3)

#Entries
webs=Entry(width=40)
webs.grid(row=1,column=1, columnspan=2)
webs.focus()
em=Entry(width=40)
em.grid(row=2,column=1, columnspan=2)
em.insert(0, "Your Default Email") #Insert your default email
psd = Entry(width=22)
psd.grid(row=3,column=1)

#Buttons
gen_pswd = Button(text= "Generate Password", fg= "Red", command=generate_pswd)
gen_pswd.grid(row=3,column=2)
add = Button(text="ADD", width=34, fg= "Green", command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()