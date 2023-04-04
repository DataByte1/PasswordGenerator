import random
import string
import tkinter as tk


def generate_password():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.extend([alpha, symbol, numbers])

    password_str = "".join(password)
    lbl.config(text=password_str)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("My Password Generator")
    root.geometry("300x300")
    
    btn = tk.Button(root, text="Generate Secure Password", command=generate_password)
    btn.grid(row=2, column=2)
    
    lbl = tk.Label(root, font=("times", 18, "bold"))
    lbl.grid(row=4, column=2)
    
    root.mainloop()
