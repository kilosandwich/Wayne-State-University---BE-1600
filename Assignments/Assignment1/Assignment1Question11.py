#Hello, you are reading the Python Assignment 1 Question 11 for Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document




"""
Question 11 (6 points)
Write a program that prompts the user to enter an integer and checks whether the number is 
divisible by both 5 and 6, divisible by just one of them (but not both), and not divisible by either 
one. Question 8 (5 points)

"""

def question11(inputint):
    if (inputint%6 == 0) and (inputint%5 ==0):
        print("divisible by both 5 and 6")
    elif (inputint%6 == 0):
        print("divisble by only 6")
    elif (inputint%5 == 0):
        print("divisble by only 5")
    else:
        print("divisible by neither 5 or 6")

print("Input the number to determine if it is divisible by 5 or 6")
inputint = int(input())
question11(inputint)

