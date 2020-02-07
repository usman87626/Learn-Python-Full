# Lets create Class for Node
#It will contain data as well as two pointers to attach itself with left or right subtree(child)
class Node:
    def __init__(self , value):
        self.data = value
        #Initially set to None
        self.rightChild = None
        self.leftChild = None