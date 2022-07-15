
# Import module
from tkinter import *
 
# Create object
root = Tk()
root.title('Discord 2')
root.geometry("500x500")

root.wm_attributes('-transparentcolor', root['bg'])

my_frame = Frame(root, width=200, height=200)
my_frame.pack(pady=20, ipady=20, ipadx=20)

#my_label = Label(my_frame, text="Hello World", fg='#FFFFFF', font=("Helvetica", 16))
#my_label.pack(pady=20, ipady=20, ipadx=20)

my_label2 = Label(root) 
my_label2.InputText()

root.mainloop()