#Lab  5

#This lab deals with statistics, as a result, the statistics module needs to be imported.
import statistics

"""1. Write a function that take a list of data and returns mean and the standard deviation of the 
data. """
testlist = [0,1,2,3]
def standard_Deviation(listtouse):
    listtouse = list(listtouse)
    tempaverage = 0.0
    tempsquares = 0.0
    tempstdev = 0.0
    
    #calculate the average
    for x in listtouse:
        tempaverage = tempaverage + x/(len(listtouse))
    #calculate the summation of least squares
    for x in listtouse:
        tempsquares = tempsquares + (x-tempaverage)**2
    #divide by n-1 and find the square root
    tempstdev = (tempsquares / (len(listtouse) - 1))**(0.5)
    outputlist = [tempaverage,tempstdev]
    return outputlist
print(standard_Deviation(testlist))

#Create a dictionary from 2 lists
"""2 .Create a dictionary from following lists: [1,2,3,4,], [‘a’,’b’,’c’,’d’]"""

x = [1,2,3,4]
y = ["a", "b", "c", "d"]

def dictionary_duo(list01,list02):
    tempdict = dict(zip(list01,list02))
    return tempdict

print(dictionary_duo(x,y))

"""3. Write a Python program to sum all the item values in a dictionary."""
#sum all the item values in a dictionary

testdictionary = {"potato":1, "tomato":2}
def item_adder(inputdictionary):
    tempvalues = inputdictionary.values()
    tempsum = 0.0
    for x in tempvalues:
        tempsum = tempsum + x
    return tempsum
print(item_adder(testdictionary))
        
"""4. Write a Python program to create a dictionary from a string. Value is the count of the 
letters from the string.
Sample string: ‘helloworld2022!’
Expected output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '2': 3, '0': 1}"""
#create a dictionary from a string, value is the count of letters from the string

teststring = "helloworld2022!"
def string_Letter_Counter_Dictionaryifier(inputstring):
    #step one, we need two lists or this will not work
    templist = []
    templiststring = list(inputstring)
    #create a blank dictionary, we can count the values later
    for x in inputstring:
        templist.append(0)
    
    tempdict = dict(zip(templiststring.copy(),templist.copy()))
    
    #Duplicates of letters removed, now count how many times they appear in the initial string. 
    templetters = tempdict.keys()
    
    for x in templetters:
        tempsum = 0
        for y in inputstring:
            if x == y:
                tempsum = tempsum + 1
        tempdict.update({x:tempsum})
    print(tempdict)
    return tempdict

string_Letter_Counter_Dictionaryifier(teststring)

question5input = string_Letter_Counter_Dictionaryifier(teststring)
         
"""5. Write a function that takes the dictionary from question 4 and return the three most 
frequent characters. """
#return the 3 most frequent characters from question 4

def dictionary_top_three(inputdictionary):
    topthreelist = [0,0,0]
    tempkeys = inputdictionary.keys()
    tempvalues = inputdictionary.values()
    maxcount = max(tempvalues)

    for key,value in inputdictionary.items():
            if(value == maxcount):
                topthreelist[0] = key
    print(topthreelist)
    return topthreelist
print("Question 5:")
dictionary_top_three(question5input)


        

    

    

"""6. Write a Python program to create a set from ‘helloworld2022!’"""
#create a set from the string ("helloworld2022!")

teststring = "Helloworld2022!"
def string_to_set(inputstring):
    return (set(inputstring))
print(string_to_set(teststring))


"""7. Write a Python program to remove the intersection of a 2nd set from the 1st set."""
#remove the intersection of a 2nd set from the 1st set

testset01 = {0,1,2,3,"pie"}
testset02 = {"pie"}
def Set_Interection_Remover(inputset01,inputset02):
    tempset01 = inputset01.copy()
    tempset01 = tempset01.intersection(inputset02)
    inputset01 = inputset01 - tempset01
    return inputset01


print(Set_Interection_Remover(testset01,testset02))

"""8. Write a Python program to create tuple with the following data.
‘1’,’6’,’CS’,’Wayne’,’2022’,’November’"""
#create tuples from the following data: "1","6","CS","Wayne", "2022", "November"

testinput = "‘1’,’6’,’CS’,’Wayne’,’2022’,’November’"
def tupleifier(input01):
    return tuple(input01)

print(tupleifier(testinput))



    
        
        
    
 
        

    