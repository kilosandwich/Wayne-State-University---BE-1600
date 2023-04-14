#Hello, you are reading the Python Assignment 1 Question 10 for Phillip Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document


"""
Question 10 (5 points)
Suppose you shop for rice and find it in two different sized packages. You would like to write a 
program to compare the costs of the packages. The program prompts the user to enter the weight 
and price of each package and then displays the one with the better price. 
Here is a sample run:
Enter weight for package 1: 50
Enter price for package 1: 24.59
Enter weight for package 2: 25
Enter price for package 2: 11.99
Package 1 has the best price.
"""
def comparepackage(w1,p1,w2,p2):
    w1 = float(w1)
    w2 = float(w2)
    p1 = float(p1)
    p2 = float(p2)

    if w1/p1 <= w2/p2:
        print("package 1 is cheaper")
    else:
        print("package 2 is cheaper")

print("Enter the weight of package 1")
w1 = input()
print ("Enter the price of package 1")
p1 = input()

print ("Enter the weight of package 2")
w2 = input()
print("Enter the price of package 2")
p2 = input()
comparepackage(w1,p1,w2,p2)

