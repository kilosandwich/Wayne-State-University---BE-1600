
"""
Question 01 (10 points)
Write code to count the number of characters in original_str using the accumulation pattern and assign 
the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it 
while you are working on this problem, comment it out afterward!)
original_str = "The quick brown rhino jumped over the extremely lazy fox."
"""
from pyparsing import nums


original_str = "The quick brown rhino jumped over the extremely lazy fox."
def char_counter(charcounterinput):
    tempcounter = 0
    for char in charcounterinput:
        tempcounter += 1
    global num_chars
    num_chars = tempcounter
    print("The number of characters in the input ", '"', charcounterinput, '"', " is: ", num_chars)

char_counter(original_str)


"""
Question 02 (10 points)
addition_str is a string with a list of numbers separated by the + sign. Write code that uses the 
accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You 
can use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20"
"""
addition_str = "2+5+10+20"

def splitter(splitterinput):
    splitterinput = splitterinput.split("+")
    counterer = 0
    for x in splitterinput:
        tempx = int(x)
        counterer += tempx
    global sum_val
    sum_val = counterer
    print("The sum of the numbers in this string is: ", sum_val)

splitter(addition_str)

"""
Question 03 (10 points)
The formula for computing the final amount if one is earning compound interest is given on 
Wikipedia as
Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the 
value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for 
the number of years, t, that the money will be compounded for. Calculate and print the final amount 
after t years.
"""
#the text didn't copy and paste the picture with it

p = 10000
n = 12
r = 0.08
print("Enter the number of years to be compounded for:")
t = int(input())

def compound_Interest(pinput, ninput,rinput, tinput):
    pinput = float(pinput)
    ninput = float(ninput)
    rinput = float(rinput)
    tinput = float(tinput)
    amounttoprint = pinput*((1+(rinput/ninput))**(ninput*tinput))
    print("The money after ", tinput, " years is: ", amounttoprint)

compound_Interest(p,n,r,t)



"""
Question 04 (10 points)
Write a program that will compute MPG for a car. Prompt the user to enter the number of miles 
driven and store it in a variable called miles and the number of gallons used stored in a 
variable gallons. Print a nice message with the answer.
"""
print("Enter the number of miles driven:")
miles = float(input())
print("Enter the number of gallons used for the miles driven:")
gallons = float(input())

def MPG_calculator(milesdriveninput, gallonsinput):
    milesdriveninput = float(milesdriveninput)
    gallonsinput = float(gallonsinput)
    milespergallon = milesdriveninput/gallonsinput
    print("The number of miles per gallon is ", milespergallon)
    print("A nice message with the answer") #good joke, everybody laughs.

MPG_calculator(miles, gallons)

"""
Question 05 (10 points)
week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code 
that uses the accumulation pattern to compute the average (sum divided by number of items) and 
assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum 
or the number of items in week_temps_f) (You can use the .split(",") function to split 
by "," and float() to cast to a float).
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
"""
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

def temp_averager(tempinput):
    tempinput = tempinput.split(",")
    tempsum = 0.0
    templen = len(tempinput)
    for x in tempinput:
        tempx = float(x)
        tempsum += tempx
    averagetemp = tempsum / templen
    print("The average temperature is: ", averagetemp)

temp_averager(week_temps_f)



"""
Question 06 (10 points)
Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not 
hard code the list.
"""

def num_list_creator(nlengthtocreate):
    nlengthtocreate = int(nlengthtocreate)
    global nums
    nums = []
    for x in range(0, nlengthtocreate+1):
        nums.append(x)
    print("The list you have asked for appears as follows:")
    print(nums)

num_list_creator(67)

