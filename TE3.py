from Tkinter import *

root = Tk()
root.title(" Text Editor")
root.config(background="black")
root.wm_state("zoomed")

editor = Text(root)
editor.pack(fill=Y, expand=1)

editor.config(
    borderwidth=0,
    font= ("Helvetica", 10, "bold italic")
    foreground="green",
    background="black",
    insertbackground= "white",                     # cursor
    selectforeground= "green",                     # selection
    selectbackground= "#008000",
    wrap=WORD,                                     # use word wrapping
    width=64,
    undo=True,                                     # Tk 8.4
    )

editor.focus_set()

def file_new(event=None):
    try:
        save_if_modified()
        editor.clear()
    except Cancel:
        pass
    return "break"

mainloop()