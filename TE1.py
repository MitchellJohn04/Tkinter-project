from Tkinter import * 
from ttk import *

root = tk()
root.title ("write note" ) 


def saveas():
    try:
        with open('note.txt', 'w') as note:            #open file
            text = text_entry.get("1.0", 'end-1c')     #get text entry
            note.write(text)                           #write text to file
    except IOError as err:
        print("File error " + str(err))
         
text_entry = Text(root,width=50,height=30)             #create text editor
text_entry.grid(column=0, row=0) 
 
action = tk.Button(root, text="Save", command=saveFile)    #create button
action.grid(column=0, row=1)
action.config(width=66)
 
text_entry.focus()


root.mainloop()
