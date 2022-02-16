import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import requests

#from matplotlib.pyplot import text, title

def openNewWindow():

        
    url = "https://weatherapi-com.p.rapidapi.com/search.json"

    

    headers = {
        'user-agent':"Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "11705baa55msha8b0c69ff31fd3ep1840ebjsneb19d1645e91"
        }
        
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
    la2 = Label(newWindow,text="")
    la2.pack()

    e2 = Entry(inner_win2,width=40)
    e2.pack()
    def clicked():
        querystring = {f"q":{e2.get}}
        response = requests.request("GET", url, headers=headers, params=querystring)
        t = str(response.text)
        t = t.split('')

        y = open("try.txt","a")
        for tt in t:
            y.write(f"{tt} \n")
        myLabel = Label(inner_win2,text=f"CMD : {tt}")
        myLabel.pack()
    
    cmd_4 = Button(newWindow, text="Test Window CMD",command=clicked)
    cmd_4.place(x=50, y=50)
    myLabel1 = Label(inner_win2,text=f"API DATA : \n -------------- \n {e2.get()}")
    myLabel1.pack()
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

main = Tk()
main.title("GUI Practice")
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


dwnld = Button(t1_canvas, text="EXIT",command=test2)
dwnld.place(x=150, y=400)
exitb = Button(t1_canvas, text="NEXT",command=openNewWindow)
exitb.place(x=350, y=400)



##############################################################################
# tab 2
##############################################################################


##############################################################################
#bottom under display
##############################################################################

bottom_status = Label(main,text="Bottom Status Bar")
bottom_status.pack()

main.mainloop()