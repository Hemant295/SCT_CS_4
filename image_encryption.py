import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random
import os

class ImageEncryptorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.geometry("500x600")
        self.image_path = None

        self.label = tk.Label(root, text="Image Encryption Tool", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.key_label = tk.Label(root, text="Enter Key (number):")
        self.key_label.pack()

        self.key_entry = tk.Entry(root)
        self.key_entry.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=5)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack(pady=5)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if path:
            self.image_path = path
            image = Image.open(path).resize((200, 200))
            self.tk_img = ImageTk.PhotoImage(image)
            self.img_label.configure(image=self.tk_img)
            messagebox.showinfo("Loaded", "Image loaded successfully!")

    def encrypt(self):
        if not self.image_path or not self.key_entry.get().isdigit():
            messagebox.showerror("Error", "Please load an image and enter a valid key!")
            return
        key = int(self.key_entry.get())
        output_path = os.path.splitext(self.image_path)[0] + "_encrypted.png"
        self.encrypt_image(self.image_path, output_path, key)
        messagebox.showinfo("Encrypted", f"Encrypted image saved as:\n{output_path}")

    def decrypt(self):
        if not self.image_path or not self.key_entry.get().isdigit():
            messagebox.showerror("Error", "Please load an encrypted image and enter the correct key!")
            return
        key = int(self.key_entry.get())
        output_path = os.path.splitext(self.image_path)[0] + "_decrypted.png"
        self.decrypt_image(self.image_path, output_path, key)
        messagebox.showinfo("Decrypted", f"Decrypted image saved as:\n{output_path}")

    def encrypt_image(self, image_path, output_path, key):
        img = Image.open(image_path)
        pixels = list(img.getdata())
        random.seed(key)
        encrypted_pixels = [tuple((value ^ key) % 256 for value in px) for px in pixels]
        indices = list(range(len(encrypted_pixels)))
        random.shuffle(indices)
        shuffled_pixels = [encrypted_pixels[i] for i in indices]
        enc_img = Image.new(img.mode, img.size)
        enc_img.putdata(shuffled_pixels)
        enc_img.save(output_path)

    def decrypt_image(self, encrypted_path, output_path, key):
        img = Image.open(encrypted_path)
        pixels = list(img.getdata())
        random.seed(key)
        indices = list(range(len(pixels)))
        random.shuffle(indices)
        unshuffled = [None] * len(pixels)
        for i, idx in enumerate(indices):
            unshuffled[idx] = pixels[i]
        decrypted_pixels = [tuple((value ^ key) % 256 for value in px) for px in unshuffled]
        dec_img = Image.new(img.mode, img.size)
        dec_img.putdata(decrypted_pixels)
        dec_img.save(output_path)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorGUI(root)
    root.mainloop()
