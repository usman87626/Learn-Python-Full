from stack import StackADT

# Balanced Parenthesis -> "{[()]}"  as well as every parenthesis that is closed properly
# Unbalanced -> "{[" or "]})"
# 

def is_match(par1 , par2):
    if par1 == "("  and par2 == ")":
        return True
    elif par1 == "[" and par2 == "]":
        return True
    elif par1 == "{" and par2 == "}":
        return True
    else:
        return False

def checkParenthesis(paren_string):
    s = StackADT()
    is_balanced = True
    index = 0
    
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                top = s.pop()
                print(top)
                if not is_match(top , paren):
                    is_balanced = False
        index += 1
    
    if s.isEmpty() and is_balanced:
        return True
    else:
        return False    
 
 
if __name__ == "__main__":    
    bracket = input("Enter A String:") 
    answer = checkParenthesis(bracket)

    if answer == True:
        print("The Entered input has a balanced brackets")
    else:
        print("The Entered input has unbalanced brackets")