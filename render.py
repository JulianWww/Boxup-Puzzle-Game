import tkinter as tk
from levels import getLevel
from treeSearch import Tree

class Renderer:
    scale = 100
    def __init__(self, board):
        self.board = board
        self.root = tk.Tk()
        self.root.geometry(f'1000x1000')
        self.root.title('Canvas Demo - Rectangle')
        self.root.bind("<Key>", self.key_pressed)

        self.canvas = tk.Canvas(self.root, width=1000, height=1000, bg='white')
        self.canvas.pack(anchor=tk.CENTER, expand=True)
    
    def render(self):
        self.canvas.delete("all")
        self.scale = 1000 / max(len(self.board.arr), len(self.board.arr[0]))
        for x, row in enumerate(self.board.arr):
            for (y, cell) in enumerate(row):
                self.canvas.create_rectangle(self.toCanvasCords(x,y), self.toCanvasCords(x+1, y+1), fill="black" if cell else "lightgrey", outline="black")
        
        for box in self.board.boxes:
            box.render(self.canvas, self.toCanvasCords)
        self.board.cursor.render(self.canvas, self.toCanvasCords)
    
    def mainloop(self):
        self.render()
        self.root.mainloop()

    def key_pressed(self, event):    
        self.render()
    
    def toCanvasCords(self, x, y):
        return x*self.scale, y*self.scale


class PlayRenderer(Renderer):
    def __init__(self, board):
        super(PlayRenderer, self).__init__(board)
    
    def key_pressed(self, event):
        self.board.moveId(event.keycode)
        return super(PlayRenderer, self).key_pressed(event)
    
class AutoPlayRenderer(Renderer):
    def __init__(self):
        self.lvl = 1
        super(AutoPlayRenderer, self).__init__(getLevel(self.lvl))
        self.generateActions()
    
    def generateActions(self):
        tree = Tree()
        self.actions = list(tree.search(self.board))
    
    def nextLvl(self):
        self.lvl+=1
        self.board = getLevel(self.lvl)
        if (self.board is None):
            self.root.quit()
            return True
        self.generateActions()
        return False
    
    def key_pressed(self, event):
        if (len(self.actions)):
            self.board.moveId(self.actions[0])
            del self.actions[0]
        else:
            if (self.nextLvl()):
                return;
        return super(AutoPlayRenderer, self).key_pressed(event)