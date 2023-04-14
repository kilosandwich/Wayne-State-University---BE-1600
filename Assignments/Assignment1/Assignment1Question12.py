#Hello, you are reading the Python Assignment 1 Question 12 for Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document


"""
Question 12 (5 points)
Write a program that lets the user guess whether a flipped coin displays the head or the tail. The 
program randomly generates an integer 0 or 1, which represents head or tail. The program 
prompts the user to enter a guess and reports whether the guess is correct or incorrect.
Here are two sample runs:
Guess head or tail? Enter 0 for head and 1 for tail: 1
1
Correct guess
Guess head or tail? Enter 0 for head and 1 for tail: 1
0
Sorry, it is a head
"""

import random
def coinflip(guess):
    headsortails = random.randint(0,1)
    if guess == headsortails:
        "correct guess"
    else:
        if headsortails == 1:
            print("sorry, it is a tails")
        else:
            print("sorry, it is a heads")

print("Please guess 0 or 1, 0 is heads, tails is 1:")
guess = int(input())
coinflip(guess)