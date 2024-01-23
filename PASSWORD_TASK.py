import secrets
import string
import tkinter

set1 = list(string.ascii_letters)
set2 = set1 + [str(i) for i in range(10)]
set3 = set2 + list(string.punctuation)

def PasswordGenerator():
    length = int(length_var.get())
    complexity = int(complexity_var.get())
    
    if complexity == 1:
        passkey1 = ''.join(secrets.choice(set1) for _ in range(length))
        result_var.set("Password is: " + passkey1)
    
    elif complexity == 2:
        passkey2 = ''.join(secrets.choice(set2) for _ in range(length))
        result_var.set("Password is: " + passkey2)
    
    elif complexity == 3:
        passkey3 = ''.join(secrets.choice(set3) for _ in range(length)) 
        result_var.set("Password is: " + passkey3)
    
    else:
        result_var.set("Enter a valid choice for complexity!")
    
def copypassw():
    generated_password = result_var.get().split(": ")[1]
    myw.clipboard_clear()
    myw.clipboard_append(generated_password)
    myw.update()

myw = tkinter.Tk() 
myw.geometry('400x250')
myw.title('Password Generator')
myw.configure(bg='cyan', relief='groove')

length_var = tkinter.StringVar()
complexity_var = tkinter.StringVar()
result_var = tkinter.StringVar()

l1 = tkinter.Label(myw, text='Enter the desired length: ')
l1.pack(padx=1, pady=1)

e1 = tkinter.Entry(myw, textvariable=length_var)
e1.pack(padx=2, pady=2)

l2 = tkinter.Label(myw, text='Enter the desired complexity (1, 2, or 3): ')
l2.pack(padx=3, pady=3)

e2 = tkinter.Entry(myw, textvariable=complexity_var)
e2.pack(padx=4, pady=4)

generate_button = tkinter.Button(myw, text="Generate Password", command=PasswordGenerator)
generate_button.pack(padx=5, pady=5)

result_label = tkinter.Label(myw, textvariable=result_var)
result_label.pack(padx=6, pady=6)

cb1 = tkinter.Button(myw,text = "COPY", command = copypassw)
cb1.pack(padx = 7, pady = 7)

myw.mainloop()
