##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#70 point outline of house and roof
rectangle1 = drawpad.create_rectangle(200,200,400,400,fill="red")
line1 = drawpad.create_line(200,200,300,100)
line2 = drawpad.create_line(300,100,400,200)
#80 point windows and door
window1 = drawpad.create_rectangle(225,300,275,250,fill="white")
window2 = drawpad.create_rectangle(325,300,375,250,fill="white")
door = drawpad.create_rectangle(275,400,325,325,fill="white")
#90 point doorknob and chimney
doorknob = drawpad.create_oval(285,360,295,370,fill="white")
line3 = drawpad.create_line(225,175,225,50)
line4 = drawpad.create_line(250,150,250,50)
line5 = drawpad.create_line(225,50,250,50)
#100 point grass and house color
grass = drawpad.create_rectangle(200,400,400,500, fill="green")





root.mainloop()

