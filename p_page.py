from tkinter import *
import tkinter as tk





prodmaster = Tk()
prodmaster.geometry("1000x500")



tk.Label(prodmaster, text="Item No", relief=SUNKEN).grid(row=0)
e0 = tk.Entry(prodmaster).grid(row=0, column=1)

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

s = (str(e0), str(e1), str(e2), str(e3), str(e4), str(e5), str(e6))


#opens file and adds new inventory item
def save_data(s):
    save_file(s)

def save_file(x):
    e = open("item","w")
    e.write(str(s))
    e.close()

tk.Button(prodmaster,text='Cancel',command=prodmaster.quit).grid(row=19,column=0,sticky=tk.W,pady=4,padx=4)
tk.Button(prodmaster,text='Save (F2)', command=save_data(s)).grid(row=19,column=1,sticky=tk.W,pady=4,padx=4)


file = open("item", "r")
print(file.readline())

#prodmaster.config(menu=menubar)
prodmaster.mainloop()