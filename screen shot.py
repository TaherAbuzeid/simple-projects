import tkinter as tk
from tkinter.filedialog import *
import pyautogui

window = tk.Tk()


window.geometry("300x100")
window.title("screen shot")


def work():
    shot = pyautogui.screenshot()
    image = asksaveasfilename()
    shot.save(image + " ss.png")


b = tk.Button(window, text="Click me !! ", bg="black", fg="white",
              font=("Arail", 15, "bold"), command=work).place(x=60, y=20)


window.mainloop()
