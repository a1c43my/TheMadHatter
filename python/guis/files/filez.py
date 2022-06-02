import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import os,time

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=f"you selected\n{filename}"
    )
    #time.sleep(1)
    if(str(filename[-4:] == ".txt")):
        showinfo(
        title='File Opener',
        message="text/word file, opening with notepad"
            )   
        os.system(f"notepad.exe {filename}")
    elif( ( str(filename[-4:]==".xls") or str(filename[-4:]=="csv") ) ):
        showinfo(
        title='File Opener',
        message="excel/CSV file detected"
            )   
        os.system(f"notepad.exe {filename}")
    else:
        showinfo(
        title='File Opener',
        message=f"Unspported file selected {filename[-4:]}"
            )   


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()
