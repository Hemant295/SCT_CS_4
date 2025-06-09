import tkinter as tk
from tkinter import messagebox
import re
import pyperclip

def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"

def evaluate():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    strength, color = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

def copy_to_clipboard():
    password = entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "Nothing to copy.")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 14), width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=evaluate, bg="lightblue").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
