#!/usr/bin/env python

import tkinter as tk

def getClick():
    print("you've clicked the box!")
    struff = entry1.get()

    # clear the output box
    output.delete(0.0, tk.END)
    try:
        print("using def box")
        definition = my_compdictionary[struff]
    except:
        definition = "sorry there is no word like that, please try again."
    output.insert(0.0, definition)

def close_window():
    root.destroy()
    exit()

root = tk.Tk()
root.title("my title! :)")
root.configure(background="black")

image1=tk.PhotoImage(file="pixel_1.png")
tk.Label( root , image=image1 , bg="black" ).grid( row=0 , column=0)
tk.Label( root , text="This is another label" , bg="black" , fg="white" , font="none 12 bold" ).grid( row=1 , column=0 , sticky='NW')

entry1 = tk.Entry( root , width=20 , bg="white")
entry1.grid(row=2 , column=0 , sticky="E")

tk.Button(root , text="Submit" , width=6 , command=getClick).grid(row=3 , column=2 , sticky="NE")

# yet another label
definitionBox = tk.Label( root , text="\nDefinition" , bg="black" , fg="white" , font="none 12 bold" )
definitionBox.grid( row=4 , column=0 , sticky='W')

# output text box stuff
output = tk.Text(root, width=75, height=6 , wrap="word", background="white")
output.grid(row=5,column=0,columnspan=2,sticky="W")

# dictionary of stuff
my_compdictionary = {
    'algorithm' : 'Step by Step instructions to complete a task' , 'bug' : 'piece of code that causes a program to crash'
}

# make an exit label
tk.Button( root , text="click to exit" , font="none 12 bold" , command=close_window ).grid( row=6 , column=0 , sticky='NW')

# make the window continuous
root.mainloop()
