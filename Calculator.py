from tkinter import *
        
show_num = ""

def check_zero():
    global show_num
    show_num = show_num.lstrip("0")

def input(num):
    global show_num
    show_num = str(show_num)
    show_num += str(num)
    show_text.set(show_num)

def set_blank():
    global show_num
    show_num = str(show_num)
    show_num = ""
    show_text.set(show_num)

def delete():
    global show_num
    show_num = str(show_num)
    show_num = show_num[:-1]
    show_text.set(show_num)

def calculate():
    global show_num
    show_num = str(show_num)
    check_zero()
    show_num = eval(show_num)
    show_text.set(show_num)

if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    root.geometry("400x400")
    show_text = StringVar()

    show = Entry(root, textvariable = show_text)
    show.grid(columnspan=20, ipadx=15)

    button = Button(root, text="C", height=2, width=4, command=lambda: set_blank())
    button.grid(row=1, column=1)

    button = Button(root, text="%", height=2, width=4, command=lambda: input(8))
    button.grid(row=1, column=2)

    button = Button(root, text="<del", height=2, width=4, command=lambda: delete())
    button.grid(row=1, column=3)

    button = Button(root, text="÷", height=2, width=4, command=lambda: input("/"))
    button.grid(row=1, column=4)

    button = Button(root, text="7", height=2, width=4, command=lambda: input(7))
    button.grid(row=2, column=1)

    button = Button(root, text="8", height=2, width=4, command=lambda: input(8))
    button.grid(row=2, column=2)

    button = Button(root, text="9", height=2, width=4, command=lambda: input(9))
    button.grid(row=2, column=3)

    button = Button(root, text="x", height=2, width=4, command=lambda: input("*"))
    button.grid(row=2, column=4)

    button = Button(root, text="4", height=2, width=4, command=lambda: input(4))
    button.grid(row=3, column=1)

    button = Button(root, text="5", height=2, width=4, command=lambda: input(5))
    button.grid(row=3, column=2)

    button = Button(root, text="6", height=2, width=4, command=lambda: input(6))
    button.grid(row=3, column=3)

    button = Button(root, text="-", height=2, width=4, command=lambda: input("-"))
    button.grid(row=3, column=4)

    button = Button(root, text="1", height=2, width=4, command=lambda: input(1))
    button.grid(row=4, column=1)

    button = Button(root, text="2", height=2, width=4, command=lambda: input(2))
    button.grid(row=4, column=2)

    button = Button(root, text="3", height=2, width=4, command=lambda: input(3))
    button.grid(row=4, column=3)

    button = Button(root, text="+", height=2, width=4, command=lambda: input("+"))
    button.grid(row=4, column=4)

    button = Button(root, text="00", height=2, width=4, command=lambda: input("00"))
    button.grid(row=6, column=1)

    button = Button(root, text="0", height=2, width=4, command=lambda: input(0))
    button.grid(row=6, column=2)

    button = Button(root, text=".", height=2, width=4, command=lambda: input("."))
    button.grid(row=6, column=3)

    button = Button(root, text="=", height=2, width=4, command=lambda: calculate())
    button.grid(row=6, column=4)

    root.mainloop()