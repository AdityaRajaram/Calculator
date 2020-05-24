from tkinter import *
from tkinter import PhotoImage

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value="Error!"
                print(e)
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        

    
   

root=Tk()
root.geometry("800x400")
root.title("Basic Calculator")
root.iconphoto(True, PhotoImage(file="/home/aditya/Desktop/Basic Calculator/1.png"))



#crate a string variable
scvalue = StringVar()
scvalue.set("")

#create an entry widget
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=BOTH, ipadx=8, pady=10, padx=10)
f=Frame(root,bg="orange")
for i in range(0,3):
    button=Button(f,text=f"{i+1}",padx=28,pady=18,font="lucida 35 bold",bg="white")
    button.pack(side=LEFT,padx=18,pady=5)
    button.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
for i in range(3,6):
    button=Button(f,text=f"{i+1}",padx=28,pady=18,font="lucida 35 bold",bg="white")
    button.pack(side=LEFT,padx=18,pady=5)
    button.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
for i in range(6,9):
    button=Button(f,text=f"{i+1}",padx=28,pady=18,font="lucida 35 bold",bg="white")
    button.pack(side=LEFT,padx=18,pady=5)
    button.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
button=Button(f,text="0",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(f,text="=",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(f,text="C",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
button=Button(f,text=f".",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(f,text="+",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(f,text="-",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
button=Button(f,text="*",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(f,text="/",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(f,text="%",padx=28,pady=18,font="lucida 35 bold",bg="white")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
f.pack()






root.mainloop()