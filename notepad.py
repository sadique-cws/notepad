from tkinter import *
top = Tk()
top.geometry("600x500")
top.title("Notepad by sadique")

def newFile():
    editor.delete(1.0,END)

def closeCWSNotepad():
    top.quit()

menubar = Menu(top)

fileMenu = Menu(menubar,tearoff=0)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="New Window")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As")
fileMenu.add_separator()
fileMenu.add_command(label="Page Setup")
fileMenu.add_command(label="Print\tCtrl + P")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=closeCWSNotepad)

editMenu = Menu(menubar,tearoff=0)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Cut      Ctrl+X")
editMenu.add_command(label="Copy     Ctrl+C")
editMenu.add_command(label="Paste    Ctrl+V")
editMenu.add_command(label="Delete    DEL")
editMenu.add_separator()
editMenu.add_command(label="Find    Ctrl+F")
editMenu.add_command(label="Find Next\tCtrl+F3")
editMenu.add_command(label="Find Previous\tShift+F3")
editMenu.add_command(label="Replace\t Ctrl + H")
editMenu.add_command(label="Go to\t Ctrl + G")
editMenu.add_separator()
editMenu.add_command(label="Select All\tCtrl + A")
editMenu.add_command(label="Time/Date\tF5")
editMenu.add_separator()


formatMenu = Menu(menubar,tearoff=0)
formatMenu.add_command(label="WordWrap")
formatMenu.add_command(label="Font")


viewMenu  = Menu(menubar,tearoff=0)

zoomMenu = Menu(viewMenu,tearoff=0)
zoomMenu.add_command(label="Zoom In")
zoomMenu.add_command(label="Zoom Out")

viewMenu.add_cascade(label="Zoom",menu=zoomMenu)
viewMenu.add_checkbutton(label="Status Bar")

menubar.add_cascade(label="File",menu=fileMenu)
menubar.add_cascade(label="Edit",menu=editMenu)
menubar.add_cascade(label="Format",menu=formatMenu)
menubar.add_cascade(label="View",menu=viewMenu)

editor = Text(top,width=600)
editor.pack()

footerText = StringVar()
footerText.set("Ln 1, Col 1  \t|\t100%\tWindow (CRLF) \t \t| \tUTF-8")
footer = Label(top,textvariable=footerText,bd=1,relief=SUNKEN,anchor="w",padx=10,fg="gray",font=("Arial",10))
footer.pack(side=BOTTOM,fill=X)
top.config(menu=menubar)
top.mainloop()