from BST import BST
# Checking what we've done so far
#So we are going to create object and check the functions we have created in the class
if __name__ == '__main__':
    b = BST()
    b.insertValue(100)
    b.insertValue(50)
    b.insertValue(120)
    b.insertValue(25)
    b.insertValue(75)
    b.insertValue(110)
    b.insertValue(115)
    b.insertValue(112)
    b.insertValue(200)
    b.insertValue(150)
    b.insertValue(175)
    b.insertValue(125)
    b.insertValue(130)
    b.insertValue(225)
    b.insertValue(230)
    b.print_inOrder()
    b.deleteValue(200)
    print("After Deletion:")
    b.print_inOrder()