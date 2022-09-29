from tkinter import *

root = Tk()

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    variable.set(expression)


def equal():
    global expression
    total = str(eval(expression))
    variable.set(total)
    expression = ""


def clear():
    global expression
    expression = ""
    variable.set("")


root.geometry('400x400+450+140')
root.title("Calculator")

variable = StringVar()

button0 = Button(root, text="0", command=lambda: press(0))
button0.place(x=100, y=300, height=50, width=150)

button1 = Button(root, text="1", command=lambda: press(1))
button1.place(x=100, y=250, height=50, width=50)

button2 = Button(root, text="2", command=lambda: press(2))
button2.place(x=150, y=250, height=50, width=50)

button3 = Button(root, text="3", command=lambda: press(3))
button3.place(x=200, y=250, height=50, width=50)

button4 = Button(root, text="4", command=lambda: press(4))
button4.place(x=100, y=200, height=50, width=50)

button5 = Button(root, text="5", command=lambda: press(5))
button5.place(x=150, y=200, height=50, width=50)

button6 = Button(root, text="6", command=lambda: press(6))
button6.place(x=200, y=200, height=50, width=50)

button7 = Button(root, text="7", command=lambda: press(7))
button7.place(x=100, y=150, height=50, width=50)

button8 = Button(root, text="8", command=lambda: press(8))
button8.place(x=150, y=150, height=50, width=50)

button9 = Button(root, text="9", command=lambda: press(9))
button9.place(x=200, y=150, height=50, width=50)

button_add = Button(root, text="+", command=lambda: press("+"))
button_add.place(x=250, y=300, height=50, width=50)

button_subtract = Button(root, text="-", command=lambda: press("-"))
button_subtract.place(x=250, y=250, height=50, width=50)

button_multi = Button(root, text="*", command=lambda: press("*"))
button_multi.place(x=250, y=200, height=50, width=50)

button_div = Button(root, text="/", command=lambda: press("/"))
button_div.place(x=250, y=150, height=50, width=50)

button_clear = Button(root, text="C", command=clear)
button_clear.place(x=100, y=100, height=50, width=100)

button_equal = Button(root, text="=", command=equal)
button_equal.place(x=200, y=100, height=50, width=100)

enter = Entry(root, textvariable=variable, )
enter.place(x=100, y=45, width=200, height=50)

root.mainloop()
