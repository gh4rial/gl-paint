from tkinter import *
from tkinter import ttk

LINE_LIMIT = 20

CANVAS_PADDING_NS = CANVAS_PADDING_EW = 75
DEFAULT_SP_WIDTH  = DEFAULT_SP_HEIGHT = 500

DEFAULT_LINE_WIDTH = 2

class Main:
    def __init__(self):
        print("Initializing main...")
        
        self.win = Tk()
        self.win.title("gl-paint v0.0.1")
        
        self.init_toplevel()

    def init_toplevel(self):
        print("Initializing toplevel widgets...")
        
        self.style= ttk.Style()
        self.style.configure("Main.TFrame", background="lightgrey")
        
        self.mainframe = ttk.Frame(self.win, padding=f"{CANVAS_PADDING_NS} {CANVAS_PADDING_EW}", style="Main.TFrame")
        self.mainframe.grid(column=0, row=0, sticky="nwes")

        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(0, weight=1)
        
        self.init_mainframe()
                  
    # TODO: center canvas widget when mainframe resizes
    def init_mainframe(self):
        print("Initializing mainframe widgets...")
        
        self.canvas = Canvas(self.mainframe, width=DEFAULT_SP_WIDTH, height=DEFAULT_SP_HEIGHT, borderwidth=4, relief="groove")
        self.canvas.grid(column=0, row=0)
        
        self.init_sketchpad()

    def init_sketchpad(self):
        print("Initializing sketchpad...")
        
        self.sp = Sketchpad(self.canvas)
        
        self.create_binds()
        
    def create_binds(self):
        print("Creating keybinds...")
        
        self.canvas.bind("<Button-1>", self.sp.press)
        self.canvas.bind("<B1-Motion>", self.sp.draw)
        self.canvas.bind("<B1-ButtonRelease>", self.sp.unpress)
        
    def start(self):
        print("Starting event loop...")
        
        self.win.mainloop()
        
        
class Sketchpad:
    def __init__(self, canvas):
        self.line_coords = []
        self.pressed = False
        self.canvas = canvas
        
    def press(self, event):
        self.line_coords.extend([event.x, event.y])
        self.pressed = True

    def unpress(self, event):
        self.line_coords = []
        self.pressed = False

    def draw(self, event):
        print(self.line_coords)
        
        if len(self.line_coords) > LINE_LIMIT:
            self.line_coords.reverse() 

            for _ in range(LINE_LIMIT // 2):
                self.line_coords.pop()

            self.line_coords.reverse()
            
        self.line_coords.extend([event.x, event.y])
       
        if self.pressed:
            self.canvas.create_line(self.line_coords, width=DEFAULT_LINE_WIDTH)
            

def gl_main():
    main = Main()
    main.start()

if __name__ == '__main__':
    gl_main()
