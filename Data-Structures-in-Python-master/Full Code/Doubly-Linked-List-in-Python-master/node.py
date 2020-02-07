#Node that contains data and two pointers to point next and previous element(Node)
class Node:
    def __init__(self , value):
        self.data = value
        self.next = None
        self.prev = None