from tkinter import *
from tkinter import ttk

# def savePosn(event):
#     global lastx, lasty
#     lastx, lasty = event.x, event.y
    
# def addLine(event):
#     canvas.create_line((lastx, lasty, event.x, event.y), arrow="first", width=1)
#     savePosn(event)

LINE_LIMIT = 20

class Sketchpad:
    def __init__(self, canvas):
        self.line_coords = []
        # self.pressed = False
        self.canvas = canvas

    # def press(self, event):
    #     self.line_coords.extend([event.x, event.y])
    #     self.pressed = True

    # def unpress(self, event):
    #     self.line_coords = []
    #     self.pressed = False

    def draw(self, event):
        if len(self.line_coords) > LINE_LIMIT:
            self.line_coords.reverse() 

            for _ in range(LINE_LIMIT // 2):
                self.line_coords.pop()

            self.line_coords.reverse()
            
        self.line_coords.extend([event.x, event.y])
       
        # if self.pressed:
        self.canvas.create_line(self.line_coords, width=5)
        
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
sp = Sketchpad(canvas)

# canvas.bind("<Button-1>", savePosn)
# canvas.bind("<B1-Motion>", addLine)

def bm(event):
    print("b1 motion event fired")

def p(event):
    print("press event fired")

def up(event):
    print("unpress event fired")
    
# root.bind("<Button-1>", sp.press)
root.bind("<Button1-Motion>", sp.draw)
# root.bind("<Button1-ButtonRelease>", sp.unpress)

root.mainloop()
