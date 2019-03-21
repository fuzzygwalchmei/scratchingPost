import tkinter as tk
import  tkinter.scrolledtext as tkst

myWindow = tk.Tk()
myWindow.geometry('500x500')

btnFirst = tk.Button(myWindow, text="First Button").pack(fill='both')
btnSecond = tk.Button(myWindow, text="Second Button").pack(fill='both')
btnThird = tk.Button(myWindow, text="Third Button").pack(fill='both')

txtWindow = tkst.ScrolledText(myWindow, height=20).pack(fill='both')
myWindow.mainloop()