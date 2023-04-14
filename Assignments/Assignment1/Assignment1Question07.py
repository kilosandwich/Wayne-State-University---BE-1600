#Hello, you are reading the Python Assignment 1 Question 7 for Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document



"""
Question 07 (4 points)
Write a program that prompts the user to enter a four-digit integer and displays the number in 
reverse order. 
Here is a sample run:
Enter a four-digit integer : 3125
3
1
2
5
"""


print("Enter a four digit integer:")

#This doesn't work, it is commented out. 
import math

""""
def question07(fourdigitinteger):
    fourdigitinteger = int(fourdigitinteger)
    range07 = int(len(str(fourdigitinteger)))
    for i in range (1,range07 + 1):
        printthis = (fourdigitinteger) // (10**(range07-i)) 
        printthis = math.floor(printthis)
        print(printthis)
    

inputquestion07 = input()
question07(inputquestion07)
"""

inputquestion07 = input()
question07list = [int(a) for a in str(inputquestion07)]
#print(question07list)
print("The answer to question07 is:")
for digit in question07list:
    print(digit)
