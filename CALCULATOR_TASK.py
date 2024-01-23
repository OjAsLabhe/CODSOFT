import tkinter

def button_click(button_text):
    current_text = l1.cget("text")

    if button_text == "AC":
        l1.config(text="")
    elif button_text == "<-":
        l1.config(text=current_text[:-1])
    elif button_text == "=":
        try:
            result = eval(current_text)
            l1.config(text=str(result))
        except Exception as e:
            l1.config(text="Error")
    else:
        l1.config(text=current_text + button_text)

myw = tkinter.Tk()
myw.geometry('250x250')
myw.title('CALCULATOR')
myw.configure(bg='#0B60B0')

l1 = tkinter.Label(myw, width=20, bg="#B4D4FF")
l1.place(x=0, y=0)

b1 = tkinter.Button(myw, text='AC', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("AC"))
b1.place(x=0, y=30)

b2 = tkinter.Button(myw, text='<-', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("<-"))
b2.place(x=30, y=30)

b3 = tkinter.Button(myw, text='%', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("%"))
b3.place(x=60, y=30)

b4 = tkinter.Button(myw, text='/', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("/"))
b4.place(x=90, y=30)

b5 = tkinter.Button(myw, text='7', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("7"))
b5.place(x=0, y=60)

b6 = tkinter.Button(myw, text='8', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("8"))
b6.place(x=30, y=60)

b7 = tkinter.Button(myw, text='9', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("9"))
b7.place(x=60, y=60)

b8 = tkinter.Button(myw, text='*', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("*"))
b8.place(x=90, y=60)

b9 = tkinter.Button(myw, text='4', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("4"))
b9.place(x=0, y=90)

b10 = tkinter.Button(myw, text='5', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("5"))
b10.place(x=30, y=90)

b11 = tkinter.Button(myw, text='6', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("6"))
b11.place(x=60, y=90)

b12 = tkinter.Button(myw, text='-', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("-"))
b12.place(x=90, y=90)

b13 = tkinter.Button(myw, text='1', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("1"))
b13.place(x=0, y=120)

b14 = tkinter.Button(myw, text='2', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("2"))
b14.place(x=30, y=120)

b15 = tkinter.Button(myw, text='3', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("3"))
b15.place(x=60, y=120)

b16 = tkinter.Button(myw, text='+', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("+"))
b16.place(x=90, y=120)

b17 = tkinter.Button(myw, text='0', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("0"))
b17.place(x=0, y=150)

b18 = tkinter.Button(myw, text='.', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("."))
b18.place(x=30, y=150)

b19 = tkinter.Button(myw, text='=', bg='#F0EDCF', height=1, width=2, command=lambda: button_click("="))
b19.place(x=60, y=150)

myw.mainloop()
