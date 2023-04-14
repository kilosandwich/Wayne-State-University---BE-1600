#Hello, you are reading the Python Assignment 1 Question 6 for Phillip Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document




"""
Question 06 (5 points)
Write a program that displays the following table:
 a         b         pow(a, b) 
------------------------------
1         2         1.0       
2         3         8.0       
3         4         81.0      
4         5         1024.0    
5         6         15625.0  
Use format method
"""


def question06(rows):
    print( "{0:>0s} ".format("a"), end= "" )
    print( "{0:>10s} ".format("b"), end= "" )
    print( "{0:>10s} ".format("pow(a,b)"))
    print("------------------------------")
    for i in range(1,rows+1):
        a = i
        b = i+1
        powab = (a**b)
        print( "{0:>0d}".format(a), end= "")
        print( "{0:>10d}".format(b), end="")
        print( "{0:>10d}".format(powab), )
    

question06(5)

