import tkinter as tk

class Box: 
    width = 0.08
    def __init__(self, x, y, size, opening, color):
        self.x = x
        self.y = y
        self.size = size
        self.opening = opening
        self.color = color
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def render(self, canvas, toCords):
        offset = 0.05 + 0.15 * self.size
        color = self.color
        top = toCords(self.x + offset, self.y + offset)
        bottom = toCords(self.x + 1 - offset, self.y + 1 - offset)
        
        left = toCords(self.x + offset, self.y + 1 - offset - self.width)
        right = toCords(self.x + 1 - offset, self.y + self.width + offset)

        lefttop = toCords(self.x + offset + self.width, self.y + 1 - offset)
        righttop = toCords(self.x + 1 - offset - self.width, self.y + offset)
        if (self.opening.up):
            canvas.create_rectangle(top, right, fill=color, outline=color)
        
        if (self.opening.right):
            canvas.create_rectangle(bottom, righttop, fill=color, outline=color)
        
        if (self.opening.left):
            canvas.create_rectangle(top, lefttop, fill=color, outline=color)
        
        if (self.opening.down):
            canvas.create_rectangle(bottom, left, fill=color, outline=color)
    

    def __str__(self):
        return f"{self.x},{self.y}"

