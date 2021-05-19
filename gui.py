
from tkinter import *
 
window = Tk()
window.title("Flag")
area = Canvas(window, width=880, height = 560)
 
area.create_rectangle(0, 0, 880, 560, fill="blue", outline="blue")
 
for i in range(5):
    area.create_rectangle(0+i*80, 560-3*70-i*70, 2*80+i*80, 560-i*70, fill="yellow", outline="yellow")
    area.create_rectangle(880-2*80-i*80, 560-3*70-i*70, 880-i*80, 560-i*70, fill="yellow", outline="yellow")
 
area.create_rectangle(880-6*80, 0, 880-5*80, 70, fill="yellow", outline="yellow")
 
area.pack()
window.mainloop()