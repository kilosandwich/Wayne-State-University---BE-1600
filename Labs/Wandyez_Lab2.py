#wandyez_Lab 2
#First step: copy and paste the problem statement so I can remember what the heck I am supposed to be doing.
"""
a) Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays 
the number of years and days for the minutes. For simplicity, assume a year has 365 days.   
Sample run:
Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days

"""
print("Question 1")
print("input minutes to convert into years and days")
minutestoconvert = int(input())

def minute_converter(minutes):
    days = minutes / (24*60)  
    years = int(days // (365))
    days = int(days % 365)

    print(minutes, " minutes is approximately ", years, " and ", days, " days." )

minute_converter(minutestoconvert)


"""
b) Write a program to take n from the user and calculate the sum of the following series:

"""
print("Question 2")
print("input n for series")
ntoseries = int(input())
def series_two(n):
    n = int(n)
    tempsum = 0
    if n == 0:
        print("bruh, enter an integer above 0")
    else:
        for x in range (1, n+1):
            tempsum += (1/x)
    print("The sum of this series is :", tempsum)

series_two(ntoseries)


"""
c) Write a program to take n from the user and calculate the product of the following series:

"""
print("Question 3")
print("input n for series")
ntoseries = int(input()) #yeah I'm reusing the previous code, you already got the answer so what?

def series_three(n):
    n = int(n)
    tempsum = 1
    if n == 0:
        print("bruh, enter an integer above 0")
    else:
        for x in range (1, (n*4)+1, 4):
            tempsum *= (1/(x+4))
    print("The sum of this series is :", tempsum)

series_three(ntoseries)


"""
d) Write code that uses iteration to print out the length of each element of the list stored 
in str_list.

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
"""
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

def item_length(listinput):
    for x in listinput:
        xlength = len(x)
        print( x, " is ", xlength, " characters long.")

print("Question four:")
item_length(str_list)

"""


e) Write a program that will print out the length of each item in the list as well as the first 
and last characters of the item.
Weather=[‘sunny’, ’cloudy’,’partially 
sunny’,’rainy’,’storming’,’windy’,’foggy’,’snowy’,’hailing’]
"""
Weather= ["sunny", "cloudy","partially sunny","rainy","storming","windy","foggy","snowy","hailing"]

def item_length_and_first_and_last_characters(listinput):
    for x in listinput:
        xlength = len(x)
        firstcharacter = x[0]
        lastcharacter = x[-1]
        print( x, " is ", xlength, " characters long. (including spaces)")
        print( x, "'s first character:  ", firstcharacter, ". ", x, "'s last character is ", lastcharacter)

print("Question five:")
item_length_and_first_and_last_characters(Weather)



"""
f) Write code to determine how many t’s are in the following sentences.
phrases = ["My, what a lovely day today is!","Have you mastered cooking 
yet? A tasty treat could be in your future.","Have you ever seen the 
leaves change color?"]
"""
phrases = ["My, what a lovely day today is!","Have you mastered cooking yet? A tasty treat could be in your future.","Have you ever seen the leaves change color?"]

def t_counter(listinput):
    totalt = 0
    for x in listinput:
        for char in x:
            if char == "t":
                totalt += 1
    print("The total number of the letter t in this list is:" , totalt)
print("Question six:")
t_counter(phrases)


"""
g) Write a program to separate positive and negative number from a list.
Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
"""
x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

def list_seperator(listinput):
    positivelist = []
    negativelist = []
    for x in listinput:
        tempx = float(x)
        if tempx >= 0: #positive list
            positivelist.append(x)
        else: #negative list
            negativelist.append(x)
    print("The values of the positive list are:")
    print(positivelist)
    print("The values of the negative list are:")
    print(negativelist)

print("Question 7:")
list_seperator(x)
        