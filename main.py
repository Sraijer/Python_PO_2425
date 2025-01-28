from tkinter import *

root = Tk()
root.geometry('500x350')

def buttonPressed():
    current_txt = button.cget("text")
    
    if current_txt == 'Click me!':
        button.config(text = 'Back',
                      )
    else:
        button.config(text = 'Click me!',
                      )
    

button = Button(root,
                text = 'Click me!',
                command=buttonPressed
                )
button.pack()

root.mainloop()