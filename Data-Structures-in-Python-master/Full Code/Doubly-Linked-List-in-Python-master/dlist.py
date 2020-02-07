from node import Node
#Class that contains functions for Create Read Update and Delete(CRUD operations)
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Method to Add an element to the start of LinkedList
    def insertAtStart(self , value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
    #Method to add an element at end of LinkedList
    def insertAtLast(self , value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    #Method to Print Linked List in forward direction
    def printForward(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    #Method to Print Linked List in backward Direction i.e. from tail to head        
    def printBackward(self):
        curr = self.tail
        while curr != None:
            print(curr.data)
            curr = curr.prev
    
    #Method to delete first element(Node)
    def DeleteFirst(self):
        curr = self.head
        self.head = curr.next
        self.head.prev = None
        del curr
         
    #Method to delete Last element(Node)
    def DeleteLast(self):
        curr = self.tail
        self.tail = curr.prev
        self.tail.next = None
        del curr
    
    #Search Method to search Node containing value given in the argument
    def findVal(self , value):
        if self.head == None:
            return None
        else:
            curr = self.head
            while curr != None:
                if(curr.data == value):
                    return curr
                curr = curr.next
            if curr.data != value:
                return None
    
    #Method to delete Node with given value
    def DeleteNode(self , value):
        delNode = self.findVal(value)
        
        if delNode == None:
            print("No such value found")
        elif delNode == self.head:
            self.DeleteFirst()
        elif delNode == self.tail:
            self.DeleteLast()
        else: 
            par = delNode.prev
            par.next = delNode.next
            delNode.next.prev = par
            del delNode