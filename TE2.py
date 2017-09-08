from Tkinter import *
import ttk

 
win = tk.Tk()                                                     #create instance
win.title("Write Note")                                           #add a title
 
def saveFile():
    try:
        with open('note.txt', 'w') as note: #open file
            text = text_entry.get("1.0", 'end-1c')                #get text entry
            note.write(text) #write text to file
    except IOError as err:
        print("File error " + str(err))
         
text_entry = Text(win,width=50,height=30)                         #create text editor
text_entry.grid(column=0, row=0) 
 
action = ttk.Button(win, text="Save", command=saveFile)           #create button
action.grid(column=0, row=1)
action.config(width=66)
 
text_entry.focus()

win.mainloop()                                                    #start GUI
