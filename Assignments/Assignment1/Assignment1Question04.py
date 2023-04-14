#Hello, you are reading the Python Assignment 1 Question 4 Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 




"""
#Question 04 (5 points)
#Write a program that reads a number in feet, converts it to meters, and displays the result. One 
#foot is 0.305 meters. Here is a sample run:
#Enter a value for feet: 16.5
#16.5 feet is 5.0325 meters
"""

def feet_metric(feet):
    meters = feet*0.305
    print(feet, " feet is ", meters, " meters")

print("the answer to question 05 is:")
feet_metric(16.5)

