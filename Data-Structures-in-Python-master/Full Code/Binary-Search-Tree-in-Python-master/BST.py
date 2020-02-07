from node import Node
# Lets Create a Class for the Tree
#This class will be able to manipulate Node and performs some basic input output update and delete operations on it.
#NOTE: The values that are greater than the root value are on right side of tree and values that are less than root value are on the left side of the tree
class BST:
    def __init__(self):
        #A pointer to contain address of the First Element
        self.root = None
    
    #Iterative function to add new element/value to the tree
    def insertValue(self, value):
        #Creating a Node with value equal to the value we will send in argument to function
        newNode = Node(value)
        goleft = False
        #Checking if there is no element in the tree
        if self.root == None:
            #Attaching root with our node because its the first node(element) in  the tree
            self.root = newNode
        #If there's any element
        else:
            #Initializing to traverse tree to find actual position for newNode
            child = self.root
            parent = self.root
            
            while child != None:
                #If value in child Node is greater than the newNode value, go left
                if child.data > value:
                    parent = child
                    child = child.leftChild
                #If value in child Node is less than the newNode value, go right
                elif child.data < value:
                    parent = child
                    child = child.rightChild
            #When the loop is stop, parent will be on the element where we actually have to attach newNode
            if value > parent.data:
                parent.rightChild = newNode
            else:
                parent.leftChild = newNode
    
    #Inorder Traversal
    def inOrder(self,node):
        if node == None:
            return
        else:
            self.inOrder(node.leftChild)
            print(node.data)
            self.inOrder(node.rightChild)
    #This is utility function that will call recursive function->inOrder from the main section of our code        
    def print_inOrder(self):
        self.inOrder(self.root)
    
    #Post Order Traversal    
    def postOrder(self,node):
        if node == None:
            return
        else:
            self.inOrder(node.leftChild)
            self.inOrder(node.rightChild)
            print(node.data)
    #This is utility function that will call recursive function->postOrder from the main section of our code        
    def print_postOrder(self):
        self.postOrder(self.root)
    
    #Pre Order Traversal of tree
    def preOrder(self,node):
        if node == None:
            return
        else:
            self.preOrder(node.leftChild)
            self.preOrder(node.rightChild)
            print(node.data)
    #This is utility function that will call recursive function->preOrder from the main section of our code        
    def print_preOrder(self):
        self.preOrder(self.root)
        
    #Lets write the method to search an element in the tree iteratively
    def searchTreeFor(self , value):
        if self.root == None:
            print("Sorry! No such value found in the tree...")
        else:
            #Creating temp for finding the node which has value
            temp = self.root
            #par_temp will stay behind temp i.e. it will be the parent node of the searched value node(if exist)
            par_temp = self.root
            
            while temp != None:
                if value > temp.data:
                    par_temp = temp
                    temp = temp.rightChild
                    
                elif value < temp.data:
                    par_temp = temp
                    temp = temp.leftChild
                    
                else:
                    #return both values from where this method was called
                    return temp,par_temp
            #if not found, return None
            return None,None
    #method to find Predecessor/Ancestor of a value
    #If we are going to delete a node which is let's say Root and has both the left and right child
    #Then we should be able to find the best candidate for that position and replace value of root by that
    #In this way we will delete root without disturbing the whole tree
    #So the best candidate exist on the rightmost node of left child's (OR) it can exist on leftmost node of right Child
    #So its our choice to choose from above methods (or) it depends on the situation
    #NOTE: there can be multiple tricks to delete a root value
    def findReplacement(self , node):
        temp = node
        par_temp = node
        
        temp = temp.rightChild
        while temp.leftChild != None:
            par_temp = temp
            temp = temp.leftChild
        
        return temp , par_temp
            
    #So far , we have created the Create , Display and Search Section.Now let us move towards
    #the final section i.e deletion in the binary search tree
    def deleteValue(self, value):
        #If there is no value in the tree
        if self.root == None:
            print("Sorry! There is no value to delete from the tree")
        else:
            #Search for the node where the value is present as well as its parent
            #So we will use our already created searchTreeFor() method that returns the both arguments
            node , par_node = self.searchTreeFor(value)
            #If value not found
            if not node and not par_node:
                print("Sorry! No such value found in the tree...")
            else:
                #if deleting node is leaf node
                if node.rightChild == None and node.leftChild == None:
                    #if deleting node is root node
                    if node == self.root:
                        self.root = None
                    #if deleting node is on the left side of its parent node
                    elif par_node.data > node.data:
                        par_node.leftChild = None
                    else:
                        par_node.rightChild = None
                    del node
                #if deleting node has no left child but has the right child
                elif node.rightChild != None and node.leftChild == None:
                    #if deleting node is root node
                    if node == self.root:
                        self.root = node.rightChild
                    #deleting node is on the left of parent of deleting node
                    elif par_node.data > node.data:
                        par_node.leftChild = node.rightChild
                    else:
                        par_node.rightChild = node.rightChild
                    del node
                #if deleting node has no right child but has the left child        
                elif node.rightChild == None and node.leftChild != None:
                    #if deleting node is root node
                    if node == self.root:
                        self.root = node.leftChild
                    #if deleting node is on the rightSide of its parent
                    elif par_node.data < node.data:
                        par_node.rightChild = node.leftChild
                    else:
                        par_node.leftChild = node.leftChild
                    del node
                #if deleting node has both right child and the left child        
                elif node.rightChild != None and node.leftChild != None:
                    #finding best candidate for the deleted node and its parent
                    replace, par_replace = self.findReplacement(node)
                    #if deleting node is root node
                    if node == self.root:
                        #if parent of best candidate is actually the root node
                        #it means that there is no element on the left of right node of root
                        if par_replace == self.root:
                            node.data = replace.data
                            node.rightChild = replace.rightChild
                        else:
                            node.data = replace.data
                            par_replace.leftChild = replace.rightChild
                        del replace
                    #if deleting node is not the root node    
                    else:
                        #if parent of best candidate is actually the node that we are going to delete
                        #it means that there is no element on the left of right node that we are deleting
                        if node == par_replace:
                            node.data = replace.data
                            par_replace.rightChild = replace.rightChild
                        else:
                            node.data = replace.data
                            par_replace.leftChild = replace.rightChild
                        del replace
            