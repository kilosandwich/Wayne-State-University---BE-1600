#Wandyez_Lab4
#?? Create a cipher that splits a string based on whether the position in the string is even or odd. Then combines the two seperately.

print("This is the even-odd cipher:")
print("=======================")
def encryp(inputtext):
    tempx = 1
    tempevenstring = ""
    tempoddstring = ""
    for x in inputtext:
        if tempx == 0:
            tempx = 1
            tempevenstring = tempevenstring + x
        elif tempx == 1:
            tempoddstring = tempoddstring + x
            tempx = 0
    completedcypher = tempoddstring + tempevenstring
    return completedcypher

texttoputin = "123456789"
print("The initial message text is: ", texttoputin)
print("The scrambled message is:")
print(encryp(texttoputin))

def decryp(inputtext):
    howlonginput = len(inputtext)
    tempoddstring = ""
    tempevenstring = ""
    recreatedmessage = ""
    if howlonginput % 2 == 0: #determine if the length is even or odd, this determines the midpoint to decrypt.
        midpoint = int(howlonginput /2) #even output, start dead center
        inputeven = True
    else:
        midpoint = int(howlonginput // 2)  #oddoutput, start 
        inputeven = False
    
    #recreate the even and odd strings
    for x in range(0,midpoint+1):
        tempoddstring = tempoddstring + inputtext[x]
    for x in range (midpoint+1, howlonginput):
        tempevenstring = tempevenstring + inputtext[x]
    
    #debugging tools to remember if you goofed up. 
    #print("The even string is :", tempevenstring)
    #print("The oddstring is :", tempoddstring)
    
    #rebuild the initial message
    for x in range(0, midpoint):
        recreatedmessage = recreatedmessage+ tempoddstring[x] + tempevenstring[x]
    if inputeven == False:
        recreatedmessage = recreatedmessage + tempoddstring[-1]
    return recreatedmessage

print("The unscrambled message is:")
print(decryp(encryp(texttoputin)))


#Random cipher question


print("")
print("This is the random cipher section:")
print("=======================")

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipherkey = "bruh"

testtext = "ayy lmao"
print("The test text is:")
print(testtext)

import random
def alphabet_Cipher(inputtext , cipherkey):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    scrambledmessage = ""
    for x in inputtext:
        alphabetindex = alphabet.find(x) #first step, figure out where in the alphabet the number is
        #next step, plug in the equivalent
        if (alphabetindex <= len(cipherkey)) and (alphabetindex >= 0) :  
            scrambledmessage = scrambledmessage + cipherkey[alphabetindex]
        else:
            scrambledmessage = scrambledmessage + x
    print("The scrambled text based on the input: ", inputtext, " and the key: ", cipherkey, " is: " )
    return scrambledmessage

print("The scrambled message based on the key ", cipherkey, " is:")
print(alphabet_Cipher(testtext, cipherkey))
print(alphabet_Cipher("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))
print(alphabet_Cipher("abcdefghijklmnopqrstuvwxyz", "ouwckbjmpzyexavrltsfgdqihn"))
        
#4. Write a program to split a given string on hyphens and display each substring

print("")
print("This is the split hyphens section:")
print("=======================")

testtext = " Bruh' look at muh' hyphens I's got's so many"
print("The test text is:")
print(testtext)
def hyphen_Splitter(inputtext):
    templist = inputtext.split("'")
    for x in templist:
        print(x)

print("The text after hyphens are removed is:")
hyphen_Splitter(testtext)
                    
     

#5. Remove empty strings from a list of strings

print("")
print("This is the empty list remover section:")
print("=======================")
genericlistofstrings = ["", "potato", "", "tomato", ""]
print(genericlistofstrings)
def empty_string_remover(inputlist):
    templist = []
    for x in range (0, len(inputlist)):
        if inputlist[x] != "":
            templist.append(inputlist[x])
    return templist
print(empty_string_remover(genericlistofstrings))

#6. Writena  python program to remove characters which have odd index values of a given string
#please note that the problem statement indicates ALL ODD INDEX VALUES, not every other index value
print("")
print("This is the odd index remover section:")
print("=======================")

oddtester = "Wow look all the odd index values get removed"
print("The initial text before the odd numbers are removed is:")
print(oddtester)
def odd_remover(textinput):
    tempout = ""
    for x in range (0, len(textinput)):
        if x % 2 == 0: #indicates evenoutput
            tempout = tempout + textinput[x]
    return tempout
print("The text after the odd numbers are removed is:")
print(odd_remover(oddtester))

        
    
#7 Write a python sccript that takes the input from the user and displays that input back in upper and lower case

print("")
print("This is the upper and lower output section:")
print("=======================")
putinputhere = input("Input text to return in upper and lower case: ")

def upper_and_lower(textinput):
    tempupperoutput = ""
    temploweroutput = ""
    
    tempupperoutput = textinput.upper()
    temploweroutput = textinput.lower()
    print("The upper case output is: ", tempupperoutput)
    print("The lower case output is: ", temploweroutput)
    
upper_and_lower(putinputhere)
        
        
    
    
        

    

    
        
