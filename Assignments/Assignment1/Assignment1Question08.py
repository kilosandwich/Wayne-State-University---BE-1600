#Hello, you are reading the Python Assignment 1 Question 08 for Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document





""""
Question 8 (5 points)
Write a program that prompts the user to enter the side of a hexagon and displays its area. The 
formula for computing the area of a hexagon is 
where s is the length of a side. Round the area to three decimal places.
Here is a sample run:
Enter the side: 5.5
The area of the hexagon is 78.590
"""


print("Enter the side:")
sideofhexagon = float(input())

def hexagon_Area(s):
    areahexagon = 3*(3**(1/2))*0.5*s*s
    areahexagon = round(areahexagon,3)
    print(areahexagon)

print("The answer to question 08 is")
hexagon_Area(sideofhexagon)



