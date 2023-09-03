from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!!', message='Please make sure you haven\'t left any fields empty.')
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save? ')
        
        if is_ok:
            with open('Side_Projects\Password_Manager\Pwd.txt','a') as pwd_file:
                pwd_file.write(f'Website: {website} | Email: {email} | Password: {password}\n')
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title('Password Manager')
window.config(padx=60,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
lock_img = PhotoImage(file='Password_Manager\lock.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text='Website:')
website_label.grid(row=1,column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)

password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

#entries
website_entry = Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)

#buttons
genetrate_password_button = Button(text='Generate Password',width=15,command=generate_pass)
genetrate_password_button.grid(row=3,column=2)

add_pass_button = Button(text='Add',width=44,command=save)
add_pass_button.grid(row=4,column=1,columnspan=2)

window.mainloop()