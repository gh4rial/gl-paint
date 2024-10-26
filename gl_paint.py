from tkinter import *
from tkinter import ttk

import sys

LINE_LIMIT = 20

CANVAS_PADDING_NS = CANVAS_PADDING_EW = 75
DEFAULT_SP_WIDTH  = DEFAULT_SP_HEIGHT = 500

DEFAULT_PENCIL_WIDTH = 3
DEFAULT_ERASER_WIDTH = 30

class Main:
    def __init__(self):
        print("Initializing main...")
        
        self.win = Tk()
        self.win.title("gl-paint v0.0.1")
        
        self.style = ttk.Style()
        
        self.init_toplevel()

    def init_toplevel(self):
        print("Initializing toplevel widgets...")
        
        self.style.configure("Main.TFrame", background="lightgrey")
        
        self.mainframe = ttk.Frame(self.win,
                                   padding=f"{CANVAS_PADDING_NS} {CANVAS_PADDING_EW}",
                                   style="Main.TFrame")
        self.mainframe.grid(column=0, row=0, sticky="nwes")

        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(0, weight=1)
        
        self.init_mainframe()
                  
    # TODO: fix canvas when its size is larger than window size
    def init_mainframe(self):
        print("Initializing mainframe widgets...")
        
        self.canvas = Canvas(self.mainframe,
                             width=DEFAULT_SP_WIDTH,
                             height=DEFAULT_SP_HEIGHT,
                             borderwidth=4,
                             relief="groove")
        self.canvas.grid()

        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        
        self.init_sketchpad()

    def init_sketchpad(self):
        print("Initializing sketchpad...")
        
        self.sp = Sketchpad(self.canvas, self)
        
        self.create_binds()
        
    def create_binds(self):
        print("Creating keybinds...")
        
        self.canvas.bind("<ButtonPress>", self.sp.press)
        self.canvas.bind("<Motion>", self.sp.draw)
        self.canvas.bind("<ButtonRelease>", self.sp.unpress)
        
    def start(self):
        print("Starting event loop...")
        
        self.win.mainloop()

    def quit(self, code):
        self.win.destroy()
        sys.exit(code)
        
        
class Sketchpad:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.lines = []
        self.pressed = False
        
    def press(self, event):
        self.pressed = True
        
        if event.num == 1:
            self.current_line = self.new_line("pencil", "black", DEFAULT_PENCIL_WIDTH)
        elif event.num == 3:
            self.current_line = self.new_line("eraser", self.canvas.cget('background'), DEFAULT_ERASER_WIDTH)
        else:
            print(f"Mouse button {event.num} press not used")
            
        # TODO: draw dot on button press
        self.current_line['coords'].extend([event.x, event.y])

    def draw(self, event):
        if self.pressed:
            self.current_line['coords'].extend([event.x, event.y])
        
            if actual_len > LINE_LIMIT:
                actual_len = len(self.current_line['coords']) - LINE_LIMIT
            else:
                actual_len = 0
            
            actual_coords = self.current_line['coords'][actual_len:]

            self.canvas.create_line(actual_coords,
                                    width=self.current_line['width'],
                                    fill=self.current_line['color'])
        
    def unpress(self, event):
        self.lines.append(self.current_line)
        self.current_line = None
        self.pressed = False

    def new_line(self, kind, color, width):
        line = {
            'kind': kind,
            'coords': [],
            'color': color,
            'width': width,
        }

        return line

def gl_main():
    main = Main()
    main.start()

if __name__ == '__main__':
    gl_main()
