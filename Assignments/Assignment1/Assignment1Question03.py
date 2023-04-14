#Hello, you are reading the Python Assignment 1 Question 3 for Phillip Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document


"""  
#Question 03 (5 points)
#The US Census Bureau projects population based on the following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
#Write a program to display the population for each of the next five years. Assume the current 
#population is 312032486 and one year has 365 days. 
#Hint: in Python, you can use integer division operator // to perform division. The result is an 
#integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
#population after one year: 314812582
#population after two years: 317592679
#population after three years: 320372776
#population after four years: 323152873
#population after five years: 325932970
"""

def population_calculator(currentPopulation,years):
    populationseconds = 365*24*60*60 #calculate the total seconds in a year
    for i in range(1,years+1):
        populationBirths = (populationseconds*i) // 7
        populationDeaths = (populationseconds*i) // 13
        populationImmigrants = (populationseconds*i) // 45
        populationyear = populationBirths - populationDeaths +populationImmigrants
        populationyear += currentPopulation
        print("The population for year ", i, " is: ", populationyear)

print("the answer to question 03 is:")
population_calculator(312032486,5)
        
