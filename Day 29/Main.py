from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

USER_EMAIL = ""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''Generate a random password between 16 and 22 characters long'''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_input.delete(0, END)

    
    password_letters = [choice(letters) for _ in range(randint(10,12))]
    password_symbols = [choice(symbols) for _ in range(randint(3,5))]
    password_numbers = [choice(numbers) for _ in range(randint(3,5))]
    
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    
    password = "".join(password_list)
    
    password_input.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    '''Check form is filled in correctly, and save the password to a text document'''
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if len(website) <1:
        messagebox.showwarning(title="No Website Entered",message="Please enter a website and try again")
    elif len(email) <1:
        messagebox.showwarning(title="No Email Entered",message="Please enter your email and try again")
    elif len(password) <1:
        messagebox.showwarning(title="No Password Entered",message="Please enter a password and try again")
    else:
         is_okay = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\n"
                        f"Password: {password} \nIs it ok to save?")

    if is_okay:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}  |  {email}  |  {password}\n")
            website_input.delete(0,END)
            password_input.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)



canvas = Canvas(width=147, height=150)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Create labels
website_label = Label(text="Website:" )
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:" )
email_label.grid(column=0,row=2)

password_label = Label(text="Password:" )
password_label.grid(column=0,row=3)

#Create Entry bars

website_input = Entry(width=42)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

email_input = Entry(width=42)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(END, USER_EMAIL)

password_input = Entry(width=24)
password_input.grid(column=1,row=3)
#Create  buttons

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()