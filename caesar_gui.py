import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main function
def perform_action():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if choice.get() == "Encrypt":
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    output_result.config(text=f"Result: {result}")
    btn_copy.config(state="normal")  # Enable copy button
    output_result.result_text = result  # Store result for copy

# Copy to clipboard function
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(output_result.result_text)
    window.update()
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# GUI Setup
window = tk.Tk()
window.title("Caesar Cipher Encrypt/Decrypt")
window.geometry("400x350")
window.config(bg="#f0f0f0")

# Input fields
tk.Label(window, text="Enter Message:", bg="#f0f0f0").pack(pady=5)
entry_message = tk.Entry(window, width=50)
entry_message.pack(pady=5)

tk.Label(window, text="Enter Shift Value:", bg="#f0f0f0").pack(pady=5)
entry_shift = tk.Entry(window, width=10)
entry_shift.pack(pady=5)

choice = tk.StringVar(value="Encrypt")
tk.OptionMenu(window, choice, "Encrypt", "Decrypt").pack(pady=10)

tk.Button(window, text="Submit", command=perform_action).pack(pady=10)

# Output
output_result = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0f0f0")
output_result.pack(pady=10)

# Copy to clipboard button
btn_copy = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
btn_copy.pack(pady=5)

# Start GUI
window.mainloop()
