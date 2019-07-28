import tkinter as tk

def show_entry_fields():
    x,y,z = 0,0,0
    for num in range(int(e1.get()),int(e2.get())):
        if num % 3==0 and num % 5 == 0:
            print('FizzBuzz')
            x = 1+x
        elif num % 3 == 0:
            print('Fizz')
            y = 1+y
        elif num % 5 == 0:
            print('Buzz')
            z = 1+z
        else:
            print(num)

    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    #master.insert(tk.end, x, y)
    print("\nfizzbuzz count: %s\n" % x)
    print("fizz count: %s\n" % y)
    print("buzz count: %s\n" % z)
    tk.Label(master, text="fizzbuzz count: %s\n" % x ).grid(row=10)
    tk.Label(master, text="fizz count: %s\n" % y).grid(row=11)
    tk.Label(master, text="buzz count: %s\n" % z).grid(row=12)


master = tk.Tk()

tk.Label(master,
         text="First number").grid(row=0)
tk.Label(master,
         text="Last number").grid(row=1)
master.geometry("800x500")



e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,text='Quit',command=master.quit).grid(row=3,column=0,sticky=tk.W,pady=4,padx=4)

tk.Button(master,text='Show', command=show_entry_fields).grid(row=3,column=1,sticky=tk.W,pady=4,padx=4)



tk.mainloop()




