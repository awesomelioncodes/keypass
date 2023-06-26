import string
import random
import tkinter as tk

print("KeyPass GUI Beta Made by chatgpt from the original code")

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def handle_generate():
    global length_entry, password_text
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_text.config(text="Generated Password: " + password)

def generate_password_gui():
    global length_entry, password_text
    window = tk.Tk()
    window.title("Password Generator")

    length_label = tk.Label(window, text="Enter the length of the password:")
    length_label.pack()

    length_entry = tk.Entry(window)
    length_entry.pack()

    generate_button = tk.Button(window, text="Generate Password", command=handle_generate)
    generate_button.pack()

    password_text = tk.Label(window, text="Generated Password: ")
    password_text.pack()

    window.mainloop()

generate_password_gui()
