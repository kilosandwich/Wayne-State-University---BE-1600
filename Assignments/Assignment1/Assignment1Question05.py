#Hello, you are reading the Python Assignment 1 Question 4 for Wandyez
#Step 1: Copy and paste the entire assignment using a docstring, because going back and forth between a word document and VisualStudioCode is annoying
#docstrings can be created using three parentheses in a row at the beginning and end of a docstring
#Are there potentially horrible errors that could occur because docstrings are not technically comments? Yes, yes there are
#Is it easier? Yes, yes it is. 

#This entire program is very difficult to use because your instructions insisted on putting all programs together in one document



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
print("Enter the temperature in only the designated ranges so that the program works, (honors system).") #make it the user's fault if the program doesn't work. It is easier that way. 
print("Enter the temperature in Fahrenheight between -58 and 41:")
input01 = float(input())
print("Enter the wind speed in milers per hour (must be greater than or equal to 2):")
input02 = float(input())

print("the answer to question 05 is: ")
outside_temperature(input01,input02)


