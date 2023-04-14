#Hello, you are reading the Python Assignment 1 Question 2 for Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document



"""""
#Question 02 (4 points)
#π can be computed using the following formula:
#Write a program that displays the result of
#      and        
#2.9760461760461765
#3.017071817071818
"""
def Question02(howmanypi):
    positiveornegative = -1.0
    Answerquestion02 = 0
    for i in range(1,howmanypi*2+1,2):
       
        Answerquestion02 += (positiveornegative * (1/(i+2))) 
        positiveornegative *= -1.0
    Answerquestion02 += 1.0
    Answerquestion02 *= 4
    print(Answerquestion02)

print("The answer to the first part of question 2 is")
Question02(5)

print("The answer to the second part of question 2 is:")
Question02(7)


