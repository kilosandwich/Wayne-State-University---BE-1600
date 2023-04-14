#Copy the problem statement so I am not confused by it:
"""1. Write a function in python that takes a sorted list of distinct integers and a target value, then return the index if the target is found. If not, return the index where it would be if 
it were inserted in order.
"""

listquestion1 = [1,2,3,4]
def question_One(inputlist, targetvalue):
    #we are going to use the count function
    templist = inputlist.copy()
    if inputlist.count(targetvalue) > 0:
        return inputlist.index(targetvalue)
    else:
        templist.append(targetvalue)
        templist.sort()
        return templist.index(targetvalue)

print(question_One(listquestion1,5))

        
            
    






#2. Write a python function that takes two dictionaries Python program to combine two dictionary adding values for common keys. Go to the editor
#d1 = {'a': 100, 'b': 400, 'c':300, 'e':500}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: newDict({'a': 400, 'b': 600, 'd': 400, 'c': 300, 'e':500})

d1 = {'a': 100, 'b': 400, 'c':300, 'e':500}
d2 = {'a': 300, 'b': 200, 'd':400}

def question_Two(inputdictionary1, inputdictionary2):
    inputdictionary1items = inputdictionary1.items()
    inputdictionary2items = inputdictionary2.items()
    
    #Have to merge both dictionaries, but not actually touch the original dictionaries
    #I am not certain how the copying rules work, better to be paranoid
    temp1 = inputdictionary1.copy()
    temp2 = inputdictionary2.copy()
    outputdictionary = temp1.copy()
    outputdictionary.update(temp2)
    
    #now update the merged dictionary with the combined values from the original dictionary
    for key1, value1 in inputdictionary1items:
        for key2, value2 in inputdictionary2items:
            if key1 == key2:
                tempvalue = value1 + value2
                outputdictionary.update({key1:tempvalue})
    return outputdictionary
print(question_Two(d1,d2))






"""
3. Write a python function that takes a dictionary, a value and a condition (greater, less, equal) and then filters the dictionary based on values.
 
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}"""

inputdictionary3 = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

def question_Three(inputdictionary, conditionvalue, condition):
    dictionaryitems = inputdictionary.items()
    outputdictionary = {}
    for key, value in dictionaryitems:
        if condition == "greater":
            if value > conditionvalue:
                outputdictionary.update({key:value})
        elif condition == "less":
            if value < conditionvalue:
                outputdictionary.update({key:value})
        elif condition == "equal":
            if value == conditionvalue:
                outputdictionary.update({key:value})
    return outputdictionary
print(question_Three(inputdictionary3,170,"greater"))
            
            
        






"""
4. There is a dictionary of heights and weights of a group of people. Write a function that filters the value of based on the height and weight of people. 
Original Dictionary:
{'Mike: (6.1, 164), Steven: (5.9, 154), 'David: (6.0, 170), 'Sarah: (5.8, 173)}
Condition: Height > 6ft and Weight> 159pounds:
output: {'Mike: (6.2, 164)}
"""
inputdictionary4 = {'Mike': (6.1, 164), 'Steven': (5.9, 154), 'David': (6.0, 170), 'Sarah': (5.8, 173)}

def question_Four(inputdictionary, heightcondition,weightcondition):
    outputdictionary = {} #this is where we will stuff the values that meet the conditions
    dictionaryitems = inputdictionary.items()
    for key, value in dictionaryitems:
        for x in value:
            height = value[0]
            weight = value[1]
            if (height > heightcondition) and (weight > weightcondition):
                outputdictionary.update( {key:value})
    return outputdictionary

print(question_Four(inputdictionary4, 6.0, 159))







"""
5. Write a python function that takes a string and a list and puts the string at the beginning of all items in a list
Sample list : [1,2,3,4], string : hey
Expected output : ['hey1', 'hey2', 'hey3', 'hey4']"""

testlist5 = [1,2,3,4]
teststring5 = "hey"

def question_Five(inputstring,inputlist):
    for x in range(0,len(inputlist)):
        inputlist[x] = inputstring + str(inputlist[x]) 
        
    return inputlist
print(question_Five(teststring5, testlist5))