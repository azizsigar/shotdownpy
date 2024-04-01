import tkinter as tk
from tkinter import messagebox
import platform
import subprocess

def shutdown_computer():
    system = platform.system()
    if system == "Windows":
        # Windows için shutdown komutunu kullan
        subprocess.run(["shutdown", "/s", "/t", "1"])
    elif system == "Linux":
        # Linux için shutdown komutunu kullan
        subprocess.run(["sudo", "shutdown", "-h", "now"])
    else:
        messagebox.showinfo("Hata", "Bu işletim sistemi desteklenmiyor.")

def on_shutdown_button_click():
    result = messagebox.askquestion("Kapatma İşlemi", "Bilgisayarı kapatmak istediğinizden emin misiniz?")
    if result == "yes":
        shutdown_computer()

# Ana pencere oluşturma
root = tk.Tk()
root.title("Bilgisayar Kapatma Uygulaması")

# Kapatma butonu oluşturma
shutdown_button = tk.Button(root, text="Bilgisayarı Kapat", command=on_shutdown_button_click)
shutdown_button.pack(pady=20)

# Pencereyi gösterme
root.mainloop()
