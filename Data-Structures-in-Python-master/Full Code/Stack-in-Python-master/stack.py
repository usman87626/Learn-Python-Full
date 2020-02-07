class StackADT:
    # Constructor
    def __init__(self):
        # Empty list
        self.array = []
        # TOP index of the List
        self.TOP = 0

    # Method to Check whether List is empty or not
    def isEmpty(self):
        # if list is empty return true
        if self.TOP <= 0:
            return True
        # if not empty return false
        else:
            return False

    # Method to push(insert) and element to the stack
    def push(self, x):
        #Inserting value at given index i.e TOP
        self.array.insert(self.TOP, x)
        #Incrementing TOP to insert value on next Push call
        self.TOP += 1

    #Method to Pop(delete UpperMost value) from Stack
    def pop(self):
        #Check if Stack is not Empty
        if not self.isEmpty():
            #As TOP goes up after adding for next addition
            #Decreasing it to 1 to delete value that was last inserted
            self.TOP -= 1
            #Enumerating List to convert it into (index,value) pair
            for index, value in enumerate(self.array):
                #After decresing TOP , check the last Added Element
                #If matched ,return it
                if index == self.TOP:
                    return value
        #If list is empty print the message
        else:
            print("The Stack is Empty")
    
    #Check the UpperMost Value on the Stack using Same Enumeration Trick
    def Peek(self):
        if not self.isEmpty():
            #Enumerate list to (index,value) pair
            for index,value in enumerate(self.array):
                #Print value that matches with (TOP-1) index i.e. Last Added Value
                if index == (self.TOP-1):
                    print(f"The value on top of the Stack is: {value}")
        else:
            print("No item in the Stack")
    
    #Printing List in reverse Order
    #Reverse Order because 
    #We want to demonstrate that the lastly added element is at the beginning of array               
    def printWholeList(self):
        #Reversing using Slicing
        #array[startRange : EndRange : order]
        #Play with these parameters to learn more about it
        list = self.array[::-1]
        print(list)
