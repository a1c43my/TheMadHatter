import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

#from matplotlib.pyplot import text, title

# functions for creating items 

#default size 12, Times,italic/bold
def testtxt(canvas,x,y,s,fill_,text_):
    canvas.create_text(
    x,y,
    fill=fill_,
    font=f"Times {s} italic bold",
    text=text_)
def testrec(canvas,x1,y1,x2,y2,outline_,fill_):
    canvas.create_rectangle(x1, y1, x2, y2,outline=outline_,fill=fill_)

def testcir(canvas,x,y,r1,r2,fill_): # x,y, r1,r2
    canvas.create_oval(
    x, y, r1,r2,
    fill=fill_
    #tag="circ"
    )


# function for main prog bar
def start_data():
    for prog in range(20):
        tab1can.update_idletasks()
        pb1['value'] += 5
        time.sleep(.1)
        #if pb1['value'] == 30:
        

# function for progress bar
def cmd_issued():
    start_data()

#open a window 
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(tab1can)
 
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
    cmd_4 = Button(newWindow, text="Test Window CMD",command=clicked)
    cmd_4.place(x=50, y=50)

        

#def main():

main_win = Tk()
main_win.title("Interface Project Demo")
main_win.geometry("1000x700")

pb1 = Progressbar(main_win,orient=HORIZONTAL,length=100,mode='determinate')
pb1.pack(expand=True)#################################
#################################
# TITLE BOX
#################################
_label = Label(main_win,text="HS Monitor Display")
_label.pack() # to make it above main canvas
#################################
#MAIN CANVAS
#################################
# main canvas area for the background
inner_win1 = Canvas(main_win,height=750,width=1100,bg="#000")
inner_win1.pack()
##################
tabs = Notebook(inner_win1)

tab1 = Frame(tabs)
tab2 = Frame(tabs)
tab3 = Frame(tabs)

tabs.add(tab1,text="General HS")
tabs.add(tab2,text="Detailed (in work)")
tabs.add(tab3,text="Command History (in work)")
tabs.pack(expand=1,fill="both")


tab1can = Canvas(tab1,height=650,width=950,bg="#000")
tab2can = Canvas(tab2,height=650,width=950,bg="#000")
tab3can = Canvas(tab3,height=650,width=250,bg="#000")
tab1can.pack()
tab2can.pack()
tab3can.pack()



#HS Side area
#################################


#################################
#Main ER Boxes 
#################################







#################################
# TESTING
#################################

e = Entry(main_win,width=50)
e.pack()
tt = tab1can.create_text(
        300,300,
        fill="white",
        font=f"Times 12 italic bold",
        text="0 N",tags="tryme")

cmd_ = Button(tab1can, text="CMD")
cmd_.place(x=250, y=500)
cmd_2 = Button(tab1can, text="CMD w/ Status",command=start_data)
cmd_2.place(x=350, y=500)
cmd_3 = Button(tab1can, text="Test Window",command=openNewWindow)
cmd_3.place(x=450, y=500)


#################################
#BOTTOM TEXT AREA
#################################
_label2 = Label(main_win,text="Bottom Title Area")
#tab1can.after(1000,er1display)
_label2.pack() # to make it above main canvas


# text i need 

# updating telemtry values

tab1can.mainloop()
main_win.mainloop()

