from tkinter import *

def storage():
    a = entry1.get()
    return (a)

window = Tk()
window.title("Student Housing")
window.configure(width=600, height=400, bg="gray")
window.geometry("500x300")

#TENANT1 NAME AND EMAIL

t1name = Label(window, text="Tenant1 Name:", bg="gray", fg="white")
t1name.place(x=5, y = 10)
entry1 = Entry(window)
entry1.place(x=100, y = 10)

submit= Button(window, text = "Submit", command= storage)
submit.place(x=200,y=200)

print(storage())
window.mainloop()

