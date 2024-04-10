import tkinter as tk
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    user = user_entry.get()
    website = web_entry.get()
    pwd = password_entry.get()

    new_data = {
        website: {
            "email": user,
            "password": pwd
        }
    }

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showerror("Error", "Blank space!!")
    else:
        try:
            # try to read json file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update json
            data.update(new_data)
            # write to json file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clearing the text in entry boxes
            web_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(website, f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror("Error", f"No details for {website} exists")
    finally:
        # clearing the text in entry boxes
        web_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# canvas
myCanvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
myCanvas.create_image(100, 100, image=logo_img)
myCanvas.grid(column=1, row=0)

# button
generate_button = tk.Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=43, command=save_pwd)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tk.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
# entry
web_entry = tk.Entry(width=33)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = tk.Entry(width=51)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "user@email.com")

password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3)

# label
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = tk.Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

root.mainloop()
