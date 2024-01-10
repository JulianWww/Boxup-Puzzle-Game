class Opening:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

UP = Opening(False, True, True, True)
DOWN = Opening(True, False, True, True)
LEFT = Opening(True, True, False, True)
RIGHT = Opening(True, True, True, False)