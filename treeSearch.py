from copy import deepcopy
from queue import Queue
from json import dumps

directions = [111, 116, 113, 114]

class Tree:
    def __init__(self):
        self.processed = {}
        self.unprocessed = Queue();
    
    def search(self, board):
        self.unprocessed.put(board)
        self.processed[str(board)] = None
        
        done = None
        while ((not self.unprocessed.empty()) and (done is None)):
            done = self.takeSearchStep()
        if (done is None):
            return None
        return self.backtrack(done)

    def backtrack(self, endpoint):
        prevNode = self.processed[endpoint]
        if prevNode is None:
            return
        action, preveous = prevNode
        yield from self.backtrack(preveous)
        yield action


    def takeSearchStep(self):
        node = self.unprocessed.get()
        for id in directions:
            last = self.addDirection(node, id)
            if not last is None:
                return last
    
    def addDirection(self, node, id):
        next = deepcopy(node)
        next.moveId(id)
        next_id = str(next)
        
        if (next_id in self.processed):
            return
        self.unprocessed.put(next)
        self.processed[next_id] = (id, str(node))
        if next.isDone():
            return next_id