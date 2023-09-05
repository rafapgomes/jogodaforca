# Import the required libraries
from tkinter import *

class Janela():
    def __init__(self):
        





# Create an instance of tkinter frame or window
win = Tk()
win2 = Tk()

# Set the size of the tkinter window
win.geometry("1000x600")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300)
canvas.pack()

win2.geometry("1000x600")

# Create a canvas widget
canvas2=Canvas(win2, width=500, height=300)
canvas2.pack()


# Add a line in canvas widget

def criar_forca():

    canvas.create_line(100,400,100,40, fill="black", width=5)
    canvas.create_line(100,40,300,40, fill="black", width=5)
    canvas.create_line(300,40,300,100, fill="black", width=5)

    canvas2.create_line(100,400,100,40, fill="black", width=5)
    canvas2.create_line(100,40,300,40, fill="black", width=5)
canvas2.create_line(300,40,300,100, fill="black", width=5)


def cabeca():
    canvas.create_oval(275,100,325,150)

def corpo():
    canvas.create_line(300,150,300,300,fill="black", width=5)

def braco1():
    canvas.create_line(295,190,200,250,fill="black", width=5)


def braco2():
    canvas.create_line(305,190,405,250,fill="black", width=5)


def perna1():
     canvas.create_line(300,280,50,390,fill="black", width=5)

def perna2():
     canvas.create_line(300,280,550,390,fill="black", width=5)

def imprime_texto(palavra):
    Namnlbl = Label(win, text=palavra,
                font=("Arial", "11", "bold", "italic"))
    Namnlbl.pack(side="top", pady=5, padx=20)

# Create the actual entry
e = Entry(win, font=("Arial", 12), justify="center")
e.pack(side="top")

def print_entered_value():
    value = e.get()
    print("You entered :", value)
    


button = Button(win, text="Submit", command=print_entered_value)
button.pack()



win.mainloop()

win2.mainloop()