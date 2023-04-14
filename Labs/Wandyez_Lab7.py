#Phillip Wandyez BE 1600 Lab 07
"""1.) Write a python function to create a two-dimensional list that contains the names and grades 
for each student in a class, the function should first print the list in the table format and 
then return the list.
Name Course 1 Course 2
Harry 85 90
Ashley 64 73
Tina 79 58
Dave 78 68
Mike 57 91
"""
#for convenience, the list in question one has been converted into text format for easy input with the name "inputlist.txt"
#copy and paste the above list into a text file and name the file "inputlist.txt"

inputquestionone = "inputlist.txt"

def question_One(inputtxtfile):
    filetoopen = open(inputtxtfile,"r")
    #count the number of lines
    howmanylines = filetoopen.readlines()
    numberoflines = len(howmanylines)
    filetoopen.close()
    #close the file, open it again!
    
    filetoopen = open(inputtxtfile,"r")
    
    outputlist = []
    
    for x in range(0,numberoflines):   
        tempstring = filetoopen.readline()
        print(tempstring) #This satisfies the 'print in table format requirement', as the input txt file IS a table. Yay!
        templist = tempstring.split()
        outputlist.append(templist)
    outputlist.pop(0) #remove the identifier row, leaving a list of pure numbers

    return outputlist
    

question_One(inputquestionone)
    

"""
2. Write a python function that takes the above list (of the student’s names grades) and prints 
the student’s name with the highest grade at the first course and the student’s name with 
the lowers grade at the second course. 
Output sample:
Course 1: Harry with Grade 85
Course 2: Tina with Grade 58
"""

listforquestiontwo = question_One(inputquestionone)

#note to self, name is 0, course 1 is 1, course 2 is 2
def question_Two(inputlist):
    templowscore = 99999999999999999 #Well, this is prone to future errors, but this allows me to easily compare. 
    temphighscore = 0
    temphighstudent = ""
    templowstudent = ""
    for i in inputlist: 
        for j in inputlist:#I realize now that this is a mistake that is redundant, but it works anyway!
            if int(j[1]) > int(temphighscore):
                temphighscore = j[1]
                temphighstudent = j[0]
            if int(j[2]) < int(templowscore):
                templowscore = j[2]
                templowstudent = j[0]
    print("Course 1: Highest Score is ", temphighstudent, " with a score of ", temphighscore)
    print("Course 2: Lowest Score is ", templowstudent, " with a score of ", templowscore)
    
question_Two(listforquestiontwo)

"""
3. Write a python function that takes the above list and a student name and a new grade for 
both courses and  update their grades, and return the updated list. 
"""
listforquestionthree = question_One(inputquestionone)

#Blame the user so it is their fault if they use the wrong input
print("WARNING, COURSE 1 MUST BE INPUTED AS 1, COURSE 2 MUST BE INPUTED AS 2")

def question_Three(inputlist, studentname, course, newgrade):
    
    for i in inputlist:
        for j in inputlist: #This is also a redundant mistake, but it still works!
            if str(j[0]) == str(studentname):
                j[int(course)] = newgrade
    
    print("The list has been updated")
    print(inputlist)
    return inputlist

question_Three(listforquestionthree, "Harry", 1, 0 )
    


"""
4. Write a python function that takes the above list and compute the average grade for each 
course and adds it as a row at the bottom of the table.
"""
listforquestionfour = question_Three(listforquestionthree, "Harry", 1, 0 )

def question_Four(inputlist):
    #the plan, throw all columns into new list, take average
    course1grades = []
    course2grades = []
    for i in inputlist:
        
        course1grades.append(int(i[1]))
        course2grades.append(int(i[2]))
    
    import statistics
    course1average = statistics.mean(course1grades)
    course2average = statistics.mean(course2grades)
    
    inputlist.append(["Average Grade", course1average, course2average])
    print("YOUR LIST HAS BEEN UPDATED WITH AVERAGE SCORES:")
    print(inputlist)
    return inputlist

question_Four(listforquestionfour)
    

"""
5. Write a python function that takes the above list and compute the GPA for each student 
and adds it as a new column to the end of the table. 
"""
listforquestionfive = question_Four(listforquestionfour)

def question_Five(inputlist):
    for i in inputlist:
        
        tempGPA = (int(i[1])+int(i[2]))/2
        i.append(tempGPA)
    print("YOUR LIST HAS BEEN APPENDED WITH THE GPA FOR EACH STUDENT")
    print(inputlist)
    return inputlist

listforquestionsix  = question_Five(listforquestionfive)

""" 
6. Write a python function that takes the above list and create a list of the final grade using 
the following rule: 
A if Grade>=90
B if Grade >=80
C if Grade >=70
D if Grade x<70
"""

def question_Six(inputlist):
    for i in inputlist:
        for j in range (3,4): #Yeah it only grades if for the third column, I adjusted it. I originally thought you wanted each column replaced
            if int(i[j]) >= 90:
                i.append("A")
            elif int(i[j]) >= 80:
                i.append("B")
            elif int(i[j]) >= 70:
                i.append("C")             
            elif int(i[j]) < 70:
                i.append("D")
    print("YOUR GPA LIST HAS BEEN GRADED")
    print(inputlist)
    return inputlist
    
listforquestionseven = question_Six(listforquestionsix)

"""
7. Write a python function that takes the above list and export it to a csv file using the list as 
the input."""

def question_Seven(inputlist):
    import csv
    outputfile = open("outputfile.csv", "w")
    outputstring = ""
    inputlist.insert(0, ["Name:", "Course_1:", "Course_2:", "Average of Both Courses:", "Letter Grade:"]) #Why adjust previous work? Simply tag on labels at the end
    for i in range(0,len(inputlist)):
        for j in range(0,len(inputlist[i])):
            outputstring = outputstring + " " + str(inputlist[i][j]) + ","
        outputstring = outputstring + "\n" #create a new line and assume it will be written properly!
    outputfile.write(outputstring)
        
        
    print("Your list has been graded I assume!:")

question_Seven(listforquestionseven)
            
        
            
            
    


