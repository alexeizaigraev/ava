from tkinter import *
from priem import *
def click_priem():
    button_priem.config(text="meow ))")
    #text_box1.insert(0,'button prbem pressed')
    text_box1.insert(gets() + '*')
    #os.system('python ' + './app/.priem.py')

os.system('python priem.py')
root = Tk()
F = LabelFrame(borderwidth=2, text='people')
F.pack()
text_box1 = Entry(master=F, text='text_box1')
text_box1.pack()
button_priem = Button(text="Click Me", command=click_priem)
button_priem.pack()

mainloop()
