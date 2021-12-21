from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == " ":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def save_file():
    global file

    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                  "*.txt")])
        if file == " ":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")

    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quit_app():
    root.destroy()


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad made by NAMAN")


if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("note.ico")
    root.geometry("644x788")

    # Add Text Area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Create Menu Bar
    MenuBar = Menu(root)

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)

    # To open new file
    FileMenu.add_command(label="New", command=new_file)

    # To open already existing file
    FileMenu.add_command(label="Open", command=open_file)

    # To save current file

    FileMenu.add_command(label="Save", command=save_file)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quit_app)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu Ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)

    # To give feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    # Adding ScrollBar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
