from stack import StackADT

'''
 Converting a Number from Deciaml to Binary includes following steps:
 i. divide the number and store the remainder
 ii. repeat the step 1 until the number gets too small to divide
 iii. After that , print the stored remainder in reverse order
 
 So, we can store remainder in Stack and in the last we can pop elements out
 to get our answer in binary.
 That's it
'''

def decimal2binary(dec_num):
    s = StackADT()
    
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
        
    
    bin_num = " "
    while not s.isEmpty():
        bin_num += str(s.pop())
        
    return bin_num

if __name__ == "__main__":
    dec_num = input("Enter a decimal number to convert into Binary: ")
    bin_num = decimal2binary(dec_num)
    print(f"The decimal number {dec_num} in binary is {bin_num}")