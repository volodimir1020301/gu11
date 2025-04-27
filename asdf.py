from customtkinter import *


window = CTk()
window.geometry("500x500")
window.title("Logika")
window.configure(fg_color="blue")
knopka = CTkButton(window, text="Клікни")
knopka.pack()
nadpus = CTkLabel(window, text="text")
nadpus.pack()

window.mainloop()