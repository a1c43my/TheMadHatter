import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import requests

"""
def clicked():
                
    if e.get() == "ER1": 
        cmd_issued()
        myLabel = Label(inner_win2,text=f"CMD SENT: ACTIAVTE {e.get()}")
        myLabel2 = Label(tab3can,text=f"CMD SENT: ACTIAVTE {e.get()}")
    else: 
        myLabel = Label(inner_win2,text=f"CMD : {e.get()}")
        myLabel2 = Label(tab3can,text=f"CMD : {e.get()}")

    myLabel.pack()
    myLabel2.pack()

"""
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(main)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
    inner_win2 = Canvas(newWindow,height=300,width=300,bg="red")
    inner_win2.pack()
    la2 = Label(main_win,text="")
    la2.pack()

    e = Entry(inner_win2,width=40)
    e.pack()
  
    cmd_4 = Button(newWindow, text="Test Window CMD",command='clicked')
    cmd_4.place(x=50, y=50)
#default size 12, Times,italic/bold
def txt(canvas,x,y,s,fill_,text_):
    canvas.create_text(
    x,y,
    fill=fill_,
    font=f"Times {s} italic bold",
    text=text_)
def rec(canvas,x1,y1,x2,y2,outline_,fill_):
    canvas.create_rectangle(x1, y1, x2, y2,outline=outline_,fill=fill_)

def cir(canvas,x,y,r1,r2,fill_): # x,y, r1,r2
    canvas.create_oval(
    x, y, r1,r2,
    fill=fill_
    #tag="circ"
    )
def line(canvas,x,y,xx,yy):
    canvas.create_line(x, y, xx, yy)

def dline(canvas,x, y, xx, yy,dash,dspace):
    canvas.create_line(x, y, xx, yy,dash,dspace)

def dline(canvas,x, y,x2,y2,x3,y3,x4,y4):
    canvas.create_line(x, y,x2,y2,x3,y3,x4,y4)

def test2():
    print('def2')
    
def ex():
    main.close()

def load():
    requests.get()

def saveFile():
    # set it to current directory ( . )  or root ( / )s
    file = fd.asksaveasfile(initialdir="C:\\Users\\xsweeney\\Desktop\\",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window
    file.write(filetext)
    file.close()

def select_pse_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    if(str(filename).endswith(".txt")):
        showinfo(
        title='File Opener',
        message="text/word file, opening with notepad"
            )   
        #os.system(f"notepad.exe {filename}")
    elif( ( str(filename).endswith(".xlsx") or str(filename).endswith(".csv") ) ):
        showinfo(
        title='File Opener',
        message="excel/CSV file detected"
            )   
        #os.system(f"notepad.exe {filename}")
    elif( ( str(filename).endswith(".py") or str(filename).endswith(".pyi") ) ):
        showinfo(
        title='File Opener',
        message="python file detected"
            )   
        #os.system(f"notepad.exe {filename}")
    else:
        showinfo(
        title='File Opener',
        message=f"Unspported file selected {filename[-4:]}"
            )   

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('excel', '*.xlsx'),
        ('powerpoint', '*.pptx'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
main = Tk()
main.title("Notepad GUI")
main.geometry("800x800")


tp_status = Label(main,text="Top Status Bar")
tp_status.pack()
tbottom_status = Label(main,text="Exit or click Next to download files")
tbottom_status.pack()
##############################################################################
#bottom under status bar
##############################################################################

t1_canvas = Canvas(main,height=700,width=700,bg="#000")
t1_canvas.pack()


er1_frame = rec(t1_canvas,100,50,200,200,"red","lightgrey")

dwnld = Button(t1_canvas, text="NEXT",command=test2)
dwnld.place(x=250, y=400)
save = Button(t1_canvas, text="SAVE",command=test2)
save.place(x=350, y=400)
openf = Button(t1_canvas, text="OPEN",command=test2)
openf.place(x=450, y=400)
exitb = Button(t1_canvas, text="EXIT",command=test2)
exitb.place(x=550, y=400)



##############################################################################
# tab 2
##############################################################################


##############################################################################
#bottom under display
##############################################################################

bottom_status = Label(main,text="Bottom Status Bar")
bottom_status.pack()

main.mainloop()