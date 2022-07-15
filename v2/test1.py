from tkinter import *
 
root = Tk()
#root.geometry("300x300")
root.title(" Q&A ")

root.wm_attributes('-transparentcolor', root['bg'])
root.wm_attributes('-transparentcolor', 'black')

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")
     
l = Label()
inputtxt = Text(root, height = 1,
                width = 50,
                fg='#FFFFFF',
                bg = "grey")
 
Output = Text(root, height = 20,
              width = 45,
              fg='grey',
              font=("Bold", 12),
              bg = "black")
 
Display = Button(root, height = 1,
                 width = 56,
                 text ="Send",
                 bg = "dark grey",
                 command = lambda:Take_input())
 
#l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()