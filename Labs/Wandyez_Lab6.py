#Wandyez Lab 6
#Write down the name of what I am doing because I will forget it otherwise ^

#Copy the entire problem statement so I don't have to remember what I am doing.

#1. Write a python function that takes a file and an integer number n.
# The function should read the first n lines of the file line by line and store it into a list and return the list


def question_One(filetoopen, n):
    filetoread = open(filetoopen, 'r')
    outputlist = []
    tempcounter = 0
    for line in filetoread:
        if tempcounter < n:
            outputlist.append(line)
            tempcounter = tempcounter + 1 
    return outputlist

print(question_One("rainfall.txt", 5 ))
        
        
    

#2. Write a python function that takes a file and finds the longest word
# in the file and turents the word and the number of characters in the word

def question_Two(filetoopen):
    filetoread = open(filetoopen, 'r')
    filetext = filetoread.read()
    filetext = filetext.split()
    templength = 0
    tempstring = ""
    for x in filetext:
        if len(x) > templength:
            templength = len(x)
            tempstring = x
    
    outputlist = [ tempstring, templength]
    return outputlist

print(question_Two("rainfall.txt"))
    
    
    
#3. Write a python function that takes a list of string and write the contnent in a file and return the file. 

testlist = ["potato ", "tomato ", "spaghetti ", "summon the eldritch horror"]

def question_Three(inputlist):
    filetocreate = open("outputlist.txt", 'w')
    for x in testlist:
        filetocreate.write(x)
    
    filetocreate.close()
    filetoread = open("outputlist.txt", "r")
    textoffile = filetoread.read()
    return textoffile

print(question_Three(testlist))
    