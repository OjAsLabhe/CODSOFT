import tkinter

class todolist:
    def __init__(self,myw):
        self.myw = myw
        self.myw.geometry('400x400')
        self.myw.title('To-Do List')
        self.myw.configure(bg = '#80BCBD')
        self.tasklist = []
        
        self.heading = tkinter.Label(myw,text = 'To-Do LIST', font = 'courier',bg='#AAD9BB')
        self.heading.place(x = 150,y = 5)
        
        self.text1 = tkinter.Label(myw,text ='Enter The Task', font=('times new roman', 11),bg = '#F9F7C9')
        self.text1.place(x = 5, y = 60)        
        
        self.taskentry = tkinter.Entry(myw,width=20,font=('times new roman', 12))
        self.taskentry.place(x = 130,y = 60)
        
        self.taskadding = tkinter.Button(myw,text = 'Add Task',font=('courier', 10),bg = '#D5F0C1',fg = 'black', command=self.addtask)
        self.taskadding.place(x = 130 , y = 90)
        
        self.taskdelete = tkinter.Button(myw,text = 'Delete Task', font = ('courier',10),bg = '#D5F0C1',fg = 'black',command=self.deletetask)
        self.taskdelete.place(x = 220, y = 90)
        
        self.tasklistbox = tkinter.Listbox(myw,selectmode=tkinter.SINGLE, font = 'arial', bg = 'white')
        self.tasklistbox.place(x = 120, y=150)
        
    def addtask(self):
        task = self.taskentry.get()
        if task:
            self.tasklist.append(task)
            self.updatetasklist()
            self.taskentry.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning('Warning', 'No Task Entered!!')

    def updatetasklist(self):
        self.tasklistbox.delete(0, tkinter.END)
        for task in self.tasklist:
            self.tasklistbox.insert(tkinter.END, task)

    def deletetask(self):
        selected_index = self.tasklistbox.curselection()
        if selected_index:
            deleted_task = self.tasklist.pop(selected_index[0])
            self.updatetasklist()
            tkinter.messagebox.showinfo('Task Deleted', f'Task "{deleted_task}" deleted successfully.')

    

run1 = tkinter.Tk()
test = todolist(run1)
run1.mainloop()


