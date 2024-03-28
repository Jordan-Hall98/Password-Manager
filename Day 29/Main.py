from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

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

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    '''Searches database for a password relating to a website'''
    website = website_input.get()
    email = email_input.get()

    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="No Saved Passwords",message="You have no saved passwords currently")

    else:
        if len(website) <1:
            messagebox.showwarning(title="Website Error",message=f"You have not inputted a website.")
    
        elif website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showwarning(title=f"{website}",message=f"Email: {email} \nPassword: {password} \nPassword copied")
                pyperclip.copy(password)
        else:
            messagebox.showwarning(title="Invalid Key",message=f"You have not saved a password for {website}")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    '''Check form is filled in correctly, and save the password to a text document'''
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password":password,
            }
        }

    if len(website) <1 or len(email) <1 or len(password) <1:
        messagebox.showwarning(title="Missing Information",message="Please leave no fields blank")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json","w") as data_file:        
                #Creating the file
                json.dump(new_data, data_file, indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json","w") as data_file:        
                #Saving updated data
                json.dump(data, data_file, indent=4)      
        
        finally:
            website_input.delete(0,END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)



canvas = Canvas(width=147, height=150)
logo_img = PhotoImage(file="Day 29\logo.png")
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

website_input = Entry(width=24)
website_input.grid(column=1,row=1)
website_input.focus()

email_input = Entry(width=43)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(END, USER_EMAIL)

password_input = Entry(width=24)
password_input.grid(column=1,row=3)
#Create  buttons

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

search_button = Button(text="Search",command=find_password,width=15)
search_button.grid(column=2,row=1)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()