class Board: 
    lastUpdatePos = None
    def __init__(self, arr, boxes, cursor):
        self.cursor = cursor
        self.boxes = boxes
        self.arr = arr
    
    def moveId(self, id):
        if (id == 111):
            self.move(0,-1, lambda box: box.opening.down, lambda box: box.opening.up)
        elif (id == 116):
            self.move(0,1, lambda box: box.opening.up, lambda box: box.opening.down)
        elif (id == 113):
            self.move(-1,0, lambda box: box.opening.right, lambda box: box.opening.left)
        elif (id == 114):
            self.move(1,0, lambda box: box.opening.left, lambda box: box.opening.right)
    
    def getAllBoxesOnCell(self, x, y):
        return list(filter(lambda box: box.x==x and box.y==y, self.boxes))

    def isDone(self):
        if (self.lastUpdatePos is None):
            return False

        boxes = self.getAllBoxesOnCell(*self.lastUpdatePos)
        reds = list(filter(lambda box: box.color == "red", boxes))
        blues = list(filter(lambda box: box.color == "blue", boxes))
        return len(reds) and len(blues)
        
    
    def move(self, dx, dy, moveintoCheck, moveFromCheck):
        nextX = self.cursor.x + dx
        nextY = self.cursor.y + dy
        nextboxes = self.getAllBoxesOnCell(nextX, nextY)
        currentBoxes = self.getAllBoxesOnCell(self.cursor.x, self.cursor.y)

        if (not (0 <= nextY < len(self.arr) and 0 <= nextX < len(self.arr[0])) or self.arr[nextX][nextY]):
            return

        for box in nextboxes:
            if (moveintoCheck(box)):
                return
        
        currentBoxes.sort(key=lambda box: box.size)
        nextboxes.sort(key=lambda box: -box.size)
        hasLarge = False;       
        for box in currentBoxes:
            if (not hasLarge):
                if (not moveFromCheck(box)) :
                    continue
                if (len(nextboxes) > 0 and nextboxes[0].size >= box.size):
                    return
            hasLarge = True
            box.move(dx, dy)
    

        self.cursor.x = nextX
        self.cursor.y = nextY
        self.lastUpdatePos = (nextX, nextY)
    
    def __str__(self):
        return ";".join(map(str, self.boxes)) + ";" + str(self.cursor)


