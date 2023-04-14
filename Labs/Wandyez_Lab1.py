"""
1-1
Write a program that prompts the user to enter the currency exchange rate between U.S. dollars 
and Canadian dollars. Prompt the user to enter 0 to convert from U.S. dollars to Canadian dollars 
and 1 for vice versa. Prompt the user to enter the amount in U.S. dollars or Canadian dollars to 
convert it to Canadian dollars or U.S. dollars, respectively.  Round amount of money to 2 
decimal places using format method.
Here are sample runs:
Enter the exchange rate from U.S. dollars to Canadian dollars: 1.32
Enter 0 to convert U.S. dollars to Canadian dollars and 1 vice versa: 0
Enter the U.S. dollar amount: 10.75
10.75 U.S dollars is 14.19 Canadian dollars
Enter the exchange rate from U.S. dollars to Canadian dollars: 1.32
Enter 0 to convert U.S. dollars to Canadian dollars and 1 vice versa: 1
Enter the Canadian dollars amount: 14.19
14.19 Canadian dollars is 10.75 U.S. dollars
"""

import math
print("If you do not enter values in the specified ranges or as the correct types this is your fault")
#by blaming the user for me not accounting for their edge cases, I absolve my program of responsibility.
print("Please enter the current USD to CAD exchange rate")
exchangerate = float(input())
print("Please enter amount of money to convert:")
amountofmoneytoconvert = float(input())
print("Enter 0 to convert from USD to CAD.")
print("Enter 1 to convert from CAD to USD")

whichwayareweconverting = int(input())

def currency_converter(exchangeratefunction, amountofmoneytoconvertfunction, whichwayareweconvertingfunction):
    if whichwayareweconvertingfunction == 0:
        convertedmoney = amountofmoneytoconvertfunction*exchangeratefunction
        convertedmoney = round(convertedmoney,2)
        print("$", amountofmoneytoconvert, " USD is worth $", convertedmoney, " CAD")
    elif whichwayareweconvertingfunction == 1:
        convertedmoney = amountofmoneytoconvertfunction*(1/exchangeratefunction)
        convertedmoney = round(convertedmoney,2)
        print("$", amountofmoneytoconvert, " USD is worth $", convertedmoney, " CAD")

currency_converter(exchangerate, amountofmoneytoconvert, whichwayareweconverting)

"""
1-2
Write a program that prompts the user to enter the number of times (n) to roll two dices. Then 
roll the dices for n times and each time print out the two random numbers. Use the random 
module.
Here are sample runs:
Enter the number of times to roll the dice: 2
Dice 1:
3,6
Dice 2:
4,1


"""

import random
print("Enter the number of times to roll 2 dice")
amountoftimestorolldice = int(input())
def roll_the_dice(amountoftimestorolldicefunction):


    if amountoftimestorolldicefunction > 0 :
        for i in range(0,amountoftimestorolldicefunction):
            dice1roll = random.randint(0,6)
            dice2roll = random.randint(0,6)
            print("Dice 1 roll ", i+1 , " is ", dice1roll)
            print("Dice 2 roll ", i+1 , " is ", dice2roll)
    elif amountoftimestorolldicefunction == 0:
        print("You do not roll any dice, how could you do this to me. ")
    elif amountoftimestorolldicefunction < 0:
        print("You somehow roll the dice negative times, thus undoing the dice rolls of the past.\n You have shook the very fabric of reality.")

roll_the_dice(amountoftimestorolldice)
