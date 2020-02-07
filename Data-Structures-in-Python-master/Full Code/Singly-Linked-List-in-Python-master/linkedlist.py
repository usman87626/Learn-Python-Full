from node import Node
#Linked list class that contains functions for CRUD operations
class LinkList:
    #Constructor to initialize
    def __init__(self):
        self.head = None
        self.tail = None
 
    #Method to Add Element at end of last node
    def insertAtLast(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    #Method to Add Element At start of linked list
    def insertAtStart(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    #Method to delete value from start of the linked list        
    def deleteFromStart(self):
        if self.head == None:
            print("List is Empty")
        else:
            curr = self.head
            self.head = curr.next
            curr.next = None
            del curr 
            print("Value Successfully Deleted")
            
    #Method to delete last Node from Linked List        
    def deleteFromLast(self):
        last = self.tail
        if self.head == None:
            print("List is Empty")
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = None
            self.tail = curr
            del last
    
    #Method to Search for a specific value
    def searchNode(self , value):
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
            
    #Method to delete any node containing a given value
    def deleteGiven(self , delValue):
        delNode = self.searchNode(delValue)
                
        if delNode == None:
            print("Given Value Not value Found")
        elif delNode == self.head:
            self.deleteFromStart()
        elif delNode == self.tail:
            self.deleteFromLast()
        else:
            curr = self.head
            while curr.next != delNode:
                curr = curr.next
            curr.next = delNode.next
            del delNode    
    
    #Method to print the linked list     
    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
        
        
    