#Hello, you are reading the Python Assignment 1 for Phillip Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document


"""
#Question 01 (4 points)
#Write a program that displays the result of
0.8392857142857143

"""
AnswerQuestion01 = ((9.5*4.5)- (2.5*3))/(45.5-3.5)
print("The answer to Question 01 is: ")
print(AnswerQuestion01)


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

"""
#Question 05 (6 points)
#How cold is it outside? The temperature alone is not enough to provide the answer. Other factors 
#including wind speed, relative humidity, and sunshine play important roles in determining 
#coldness outside. In 2001, the National Weather Service (NWS) implemented the new wind-chill 
t#emperature to measure the coldness using temperature and wind speed. The formula is given as 
#follows:
#where ta is the outside temperature measured in degrees Fahrenheit and v is the speed measured 
#in miles per hour.  twc is the wind-chill temperature. The formula cannot be used for wind speeds 
#below 2 mph or for temperatures below or above 41°F.
W#rite a program that prompts the user to enter a temperature between -58° F and 41°F and a wind 
#speed greater than or equal to 2 and displays the wind-chill temperature rounded to two decimal 
p#laces.
H#ere is a sample run:
#Enter the temperature in Fahrenheit between -58 and 41: 5.3
#Enter the wind speed miles per hour (must be greater than or equal to 2): 6
The wind chill index is -5.57
"""
from ast import And
import math
def outside_temperature(outsideTemperature, windspeed):
    windchillTemperature = 35.74 + (0.6215*outsideTemperature)
    windchillTemperature += -35.75*(windspeed**0.16)
    windchillTemperature += 0.4275*outsideTemperature*(windspeed**0.16)
    windchillTemperature = round(windchillTemperature,2)
    print("the windchill index is: ", windchillTemperature)

print("Enter the temperature in Fahrenheight between -58 and 41:")
input01 = float(input())
print("Enter the wind speed in milers per hour (must be greater than or equal to 2):")
input02 = float(input())

print("the answer to question 05 is: ")
#outside_temperature(input01,input02)


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

#I give up I despise formatting
def question06(rows):
    print( "{0:10s} end=".format("a"), )
    print( "{0:10s} end=".format("b"), )
    print( "{0:10s} ".format("pow(a,b)"))
    print("------------------------------")
    for i in range(1,rows+1):
        a = i
        b = i+1
        powab = (a**b)
        print( "{0:0d}".format(a), end="")
        print( "{0:10d}".format(b), end= "\t")
        print( "{0:10d}".format(powab), end= "\n")

    

question06(5)

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
"""
def question07(fourdigitinteger):
    fourdigitinteger = int(fourdigitinteger)
    range07 = int(len(str(fourdigitinteger)))
    for i in range (1,range07 + 1):
        printthis = round(fourdigitinteger, i-range07) /(10**(range07-i)) 
        printthis += 
        print(printthis)
    for i in range()

inputquestion07 = input()
question07(inputquestion07)
"""


    


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




"""
Question 9 (6 points)
Suppose that x = 12, y = 34, and z = 18. Determine whether the following expressions evaluate 
to True or False.
a) 5 + 6 == 3 + 7
b) 2 * 6 - 4 >= 9 - 1
c) 6 // 3 < 3 - 1
d) 18 // 3 == 2 * 3
e) not(x - y >= 1)
f) z <= 7 or y < 12
g) (x + y != 40) and (x != z)
h) (z - x >= y) or (y - x != z + 4)
i) (5 - x <= 2 * y) and (y -15 >= z)or (x - 5 != y  - 2 * z)
j) (True and False) or not (False or False)
"""

x = 12
y = 34
z = 18

if (5 + 6 == 3 + 7):
    print("true")
else:
    print("false")
#blank space
if (2 * 6 - 4 >= 9 - 1):
    print("true")
else:
    print("false")
#blank space
if (6 // 3 < 3 - 1):
    print("true")
else:
    print("false")
#blank space
if (18 // 3 == 2 * 3):
    print("true")
else:
    print("false")
#blank space
if (not(x - y >= 1)):
    print("true")
else:
    print("false")
#blank space
if (z <= 7 or y < 12):
    print("true")
else:
    print("false")
#blank space
if ((x + y != 40) and (x != z)):
    print("true")
else:
    print("false")
#blank space
if ((z - x >= y) or (y - x != z + 4)):
    print("true")
else:
    print("false")
#blank space
if ((5 - x <= 2 * y) and (y -15 >= z)or (x - 5 != y  - 2 * z)):
    print("true")
else:
    print("false")
#blank space
if (True and False) or not (False or False):
    print("true")
else:
    print("false")
#blank space






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

    if p1/w1 <= p2/w2:
        print("package 1 is cheaper")
    else:
        print("package 2 is cheaper")

print("Enter the weight of package 1")
w1 = input()
print ("Enter the weight of package 2")
w2 = input()
print ("Enter the price of package 1")
p1 = input()
print("Enter the price of package 2")
p2 = input()
comparepackage(w1,p1,w2,p2)

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

inputint = int(input())
question11(inputint)

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
coinflip(guess=)