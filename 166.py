from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("600x600")
root.title("Drawing Tool")
root.configure(background="light blue")
label_1=Label(root,text="Enter A Color Name",bg="light blue")
label_1.place(relx=0.7,rely=0.9,anchor=CENTER)
input_1=Entry(root)
input_1.place(relx=0.8,rely=0.9,anchor=CENTER)
input_1.insert(0,"black")
img_1=ImageTk.PhotoImage(Image.open("start_point1.png"))
canvas=Canvas(root,height=510,width=590,bg="white",highlightbackground="lightgray")
canvas.pack()
canvas.create_image(50,50,image=img_1)
direction=""
oldx=50
oldy=50
newx=50
newy=50
def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="left"
    oldx=newx
    oldy=newy
    newx=newx-5
    draw(direction,oldx,oldy,newx,newy)
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="up"
    oldx=newx
    oldy=newy
    newy=newy-5
    draw(direction,oldx,oldy,newx,newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    direction="down"
    oldx=newx
    oldy=newy
    newy=newy+5
    draw(direction,oldx,oldy,newx,newy)
    
def draw(direction,oldx,oldy,newx,newy):
    fillcolor=input_1.get()
    if direction=="right":
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
    if direction=="left":
        left_line=canvas.create_line(oldx,oldy,newx.newy,width=3,fill=fillcolor)
    if direction=="up":
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
    if direction=="down":
        canvas.move(img_1,0,5)
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
        
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)
root.mainloop()