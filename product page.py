from tkinter import *
import tkinter as tk


def save_data():
    pass



prodmaster = Tk()
prodmaster.geometry("1000x500")


tk.Label(prodmaster, text="Item No", relief=SUNKEN).grid(row=0)
e1 = tk.Entry(prodmaster).grid(row=0, column=1)

tk.Label(prodmaster, text="Description", relief=RIDGE).grid(row=1)
e1 = tk.Entry(prodmaster, relief=SUNKEN).grid(row=1, column=1)

tk.Label(prodmaster, text="Price", relief=SUNKEN).grid(row=2)
e2 = tk.Entry(prodmaster, relief=SUNKEN).grid(row=2, column=1)

tk.Label(prodmaster, text="Categories", relief=SUNKEN).grid(row=3)
e3 = tk.Entry(prodmaster, relief=SUNKEN).grid(row=3, column=1)

tk.Label(prodmaster, text="Net weight", relief=SUNKEN).grid(row=4)
e4 = tk.Entry(prodmaster, relief=SUNKEN).grid(row=4, column=1)

tk.Label(prodmaster, text="Gross weight", relief=SUNKEN).grid(row=5)
e5 = tk.Entry(prodmaster, relief=SUNKEN).grid(row=5, column=1)

tk.Label(prodmaster, text="Qyt", relief=SUNKEN).grid(row=6)
e6 = tk.Entry(prodmaster, relief=SUNKEN).grid(row=6, column=1)

tk.Button(prodmaster,text='Cancel',command=prodmaster.quit).grid(row=19,column=0,sticky=tk.W,pady=4,padx=4)
tk.Button(prodmaster,text='Save (F2)', command=save_data).grid(row=19,column=1,sticky=tk.W,pady=4,padx=4)


#prodmaster.config(menu=menubar)
prodmaster.mainloop()