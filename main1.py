import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)


def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def openTaskFile():

    try:
      global task_list
      with open("tasklist.txt","r") as taskfile:
        tasks=taskfile.readlines()

      for task in tasks:
        if task!='\n':
            task_list.append(task)
            listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()

# Icon
Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# Top bar
TopImage = PhotoImage(file="Image/soft.png")
Label(root, image=TopImage).pack()

noteImage = PhotoImage(file="Image/Us.png")
Label(root, image=noteImage,bd=0).place(x=350, y=10)

heading = Label(root, text="ALL TASK", font="arial 15 bold", fg="white", bg="#DDA4DD")
heading.place(x=150, y=20)

# Main
frame = Frame(root, width=400, height=50, bg="#F6D6F6")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=20, font="ComicSans 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 15 bold", width=5, bg="#3A0849", fg="#fff", bd=0,command=addTask)
button.place(x=320, y=5)

# Listbox
list_frame1 = Frame(root, bd=3, width=380, height=280, bg="#DDA4DD")
list_frame1.place(x=10, y=240)

listbox = Listbox(list_frame1, font=('arial', 12), width=40, height=16, bg="#3A0849", bd=1,fg="white",cursor="hand2",selectbackground="#DDA4DD")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(list_frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()
#delete
Delete_icon=PhotoImage(file="Image/dust.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
root.mainloop()
