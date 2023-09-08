from tkinter import *
import tkinter.messagebox

def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c").strip()
        if not input_text:
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter some text.")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")

    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()

    button_temp = Button(root1, text="Add Task", command=add)
    button_temp.pack()

    root1.mainloop()

def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected)

def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        temp = marked[0]
        temp_marked = listbox_task.get(marked)
        temp_marked += " ✔"
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)

window = Tk()
window.title("Codsoft To-Do App")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add Task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as Completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()

# In this modified code, I've made the following changes:

#1 Removed unnecessary comments and blank lines to make the code cleaner.
#2 Adjusted the indentation for better readability.
#3 Simplified the condition for checking if the input text is empty.
#4 Added a check in the markcompleted function to ensure an item is selected before marking it as completed.
#5 Made the window title for adding tasks consistent with the rest of the application.
#6 Updated the button label for deleting tasks to be more descriptive.
#7 Added consistent spacing and indentation throughout the code.
