class Cursor:
    width = 0.1
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def render(self, canvas, coordconv):
        canvas.create_rectangle(coordconv(self.x + 0.5 - self.width, self.y + 0.5 - self.width), coordconv(self.x + 0.5 + self.width, self.y + 0.5 + self.width), fill="black")
    
    def __str__(self):
        return f"{self.x},{self.y}"