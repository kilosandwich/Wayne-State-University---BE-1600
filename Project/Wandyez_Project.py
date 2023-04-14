#Phillip Wandyez BE 1600 Final Project:
"""

0.) Name your variables so I don't have to think about them later:
"""
fileToOpen = "auto-mpg-2.csv" #there we go, that name is annoying to keep writing

import csv
import statistics
import matplotlib.pyplot as plt


"""
1.)	Reading The Dataset:
"""
#The CSV file must be imported and converted into a list.
##Use pandas csv library?

def open_And_Create_List(filetouse):
    file_open = open(filetouse, 'r')
    
    howmanylines = file_open.readlines()
    numberoflines = len(howmanylines)
    file_open.close()
    
    #I reused this section from lab 7, I did not understand the functions of csvreader so I deliberately chose to ignore it
    
    filetoopen = open(filetouse,"r")

    outputlist = []
    
    for x in range(0,numberoflines):   
        if x == 0:
            tempstring = filetoopen.readline()
            templist = tempstring.split(',')
            templist[-1] = templist[-1][:-1] #For some reason /n appears, this removes it.

            outputlist.append(templist)
            

        tempstring = filetoopen.readline()
        templist = tempstring.split(',')
        templist[-1] = templist[-1][:-1]
        outputlist.append(templist)
    outputlist.pop(-1) #for some reason the last one is a blank row. This is removed for convenience sake.
    
    #print(outputlist)
    return outputlist

#Created a list? Time to figure out why it isn't working with this handy debug function to help me find errant strings
def export_List(inputlist, exportname):
    listtoexport = inputlist.copy()
    outputfile = open(exportname, "w")
    outputstring = ""
    for i in range(0,len(inputlist)):
        for j in range(0,len(inputlist[i])):
            outputstring = outputstring + " " + str(inputlist[i][j]) + ","
        outputstring = outputstring + "\n" #create a new line and assume it will be written properly!
    outputfile.write(outputstring)



master_list = open_And_Create_List(fileToOpen)
print(master_list[0])

"""
2.)	Data Preparation:
"""
#a.	Identifying and Removing The Outlier Values:

#This function will assume a list has two dimensions, then put the desired
#column into its own list for easy analysis using statistical analysis functions
def column_To_List(inputlist, columnname):
    #Step 1, search the index 0 to determine the index to use
    columntouse = inputlist[0].index(columnname)
    templist = []
    
    #put all column items into the same list for easy analysis
    for x in range (1,len(inputlist)):
        templist.append((inputlist[x][columntouse]))
    return templist

#ListToFloat ignores null values to convert the list into a float
def list_To_Float(inputlist):
    outputlist = inputlist.copy()
    for x in range(0, len(inputlist)):
        if inputlist[x] != "":
            outputlist[x] = float(inputlist[x])
    return outputlist

def list_To_Float_NoNulls(inputlist):
    outputlist = []
    for x in range(0, len(inputlist)):
        
        if inputlist[x] != "" and inputlist[x] != " " and inputlist[x] != "." :
            outputlist.append(float(inputlist[x]))
    return outputlist


#removes the outliers from a column in a two dimensional list and returns a new list that has replaced outliers with null values. 
def outlier_Remover(inputlist, columnname):
    #convert the column absent null values for statistical purposes
    columnlist = column_To_List(inputlist, columnname)
    templist = list_To_Float_NoNulls(column_To_List(inputlist, columnname))
    tempmean = statistics.mean(templist)
    tempstdev = statistics.stdev(templist)
    
    #clean the original list with a new list
    outputlist = []
    for x in range(0,len(columnlist)):
        if columnlist[x] != "":
            #print(columnlist[x])
            tempzscore = (float(columnlist[x]) - tempmean)/tempstdev
            if abs(tempzscore) > 3.0: #value is an outlier replace with null
                outputlist.append("") #null to replace with
            else:
                outputlist.append(columnlist[x])
        else:
            outputlist.append(columnlist[x])
    return outputlist

#Updates a single column of a list with another list.
def master_List_Updater(inputmasterlist,inputlist, columnname):
    #print(columnname)
    columntouse = inputmasterlist[0].index(columnname)
    #The issue is the input list is just a list of pure numbers, therefore the master lists name must be removed and stored
    columnheader = inputmasterlist[0]
    inputmasterlist.pop(0)
    
    for x in range(0, len(inputmasterlist)):
        inputmasterlist[x][columntouse] = inputlist[x]
    
    inputmasterlist.insert(0, columnheader)



master_List_Updater(master_list, outlier_Remover(master_list,'MPG'), 'MPG')
master_List_Updater(master_list, outlier_Remover(master_list,'Cylinders'), 'Cylinders')
master_List_Updater(master_list, outlier_Remover(master_list,'Displacement'), 'Displacement')
master_List_Updater(master_list, outlier_Remover(master_list,'Horsepower'), 'Horsepower')
master_List_Updater(master_list, outlier_Remover(master_list,'Weight'), 'Weight')
master_List_Updater(master_list, outlier_Remover(master_list,'Acceleration'), 'Acceleration') 
master_List_Updater(master_list, outlier_Remover(master_list,'Model Year'), 'Model Year')
master_List_Updater(master_list, outlier_Remover(master_list,'Origin'), 'Origin')  
     
#b.	Identifying and Removing The Null Values:
#Note to self: do not eliminate an entire row just because of a null value! There is still correlation!

#TEACHER'S ORDERS, REPLACE NULL VALUES WITH MEAN VALUES. 

#The list must be processed and all "" values must be removed. 

#This function replaces all null values in a list with the mean
def null_Remover(inputlist, columnname):
    #convert the column absent null values for statistical purposes
    columnlist = column_To_List(inputlist, columnname)
    templist = list_To_Float_NoNulls(column_To_List(inputlist, columnname))
    tempmean = statistics.mean(templist.copy())
    
    #clean the original list with a new list
    outputlist = []
    for x in range(0,len(columnlist)):
        if columnlist[x] == "" or columnlist[x] == "NULL":
            outputlist.append(tempmean) #null to replace with mean
        else:
            outputlist.append(columnlist[x])
    return outputlist

master_List_Updater(master_list, null_Remover(master_list,'MPG'), 'MPG')
master_List_Updater(master_list, null_Remover(master_list,'Cylinders'), 'Cylinders')
master_List_Updater(master_list, null_Remover(master_list,'Displacement'), 'Displacement')
master_List_Updater(master_list, null_Remover(master_list,'Horsepower'), 'Horsepower')
master_List_Updater(master_list, null_Remover(master_list,'Weight'), 'Weight')
master_List_Updater(master_list, null_Remover(master_list,'Acceleration'), 'Acceleration') 
master_List_Updater(master_list, null_Remover(master_list,'Model Year'), 'Model Year')
master_List_Updater(master_list, null_Remover(master_list,'Origin'), 'Origin') 

#print(master_list)

"""
3.)	Interpreting The Data Set Using Statistic Metrics:
"""
def means_Calculator(inputmasterlist, columntouse):
    listtouse = list_To_Float(column_To_List(inputmasterlist, columntouse))
    #print(listtouse)
    meanoutput = statistics.mean(listtouse)
    return meanoutput

def medians_Calculator(inputmasterlist, columntouse):
    listtouse = list_To_Float(column_To_List(inputmasterlist, columntouse))
    medianoutput = statistics.median(listtouse)
    return medianoutput

def stdev_Calculator(inputmasterlist, columntouse):
    listtouse = list_To_Float(column_To_List(inputmasterlist, columntouse))

    stdevoutput = statistics.stdev(listtouse)
    return stdevoutput

def Bulk_Statistics(inputmasterlist):
    tempmeanslist = []
    tempmedianslist = []
    tempstdevlist = []
    for x in inputmasterlist[0]:
        tempmeanslist.append(means_Calculator(inputmasterlist, x))
        tempmedianslist.append(medians_Calculator(inputmasterlist, x))
        tempstdevlist.append(stdev_Calculator(inputmasterlist,x))
    #I will find a use for these eventually, for now this is suffiicient.
    print(tempmeanslist)
    print(tempmedianslist)
    print(tempstdevlist)
    exportlist = [inputmasterlist[0], tempmeanslist, tempmedianslist, tempstdevlist]
    export_List(exportlist, "MeansMediansStDev.csv")

Bulk_Statistics(master_list)


"""
4.)	Generating Plots For Pair Wise Correlation for Variables/Columns:
"""
def plot_machine(inputlist):
    for x in inputlist[0]: #iterate through the index row
        xaxis = list_To_Float(column_To_List(inputlist, x)) #plot the selected column against all other columns
        xlength = len(inputlist[0]) -1
        ylength = len(inputlist[0]) - 1
        plotplacement = 1
        for y in inputlist[0]:
            if x != y:
                yaxis = list_To_Float((column_To_List(inputlist,y)))
                plt.subplot(xlength, ylength, plotplacement )             
                plt.plot(xaxis, yaxis)
                #plt.title(x, " v. ", y)
                plt.xlabel(x)
                plt.ylabel(y)
                plotplacement += 1
        plt.show()

#plot_machine(master_list)
#JSON isn't connecting on my machine, I will just assume it works on yours.

                
            
                
                
"""
5.)	Providing a Pairwise Correlation Between Variables Using the Pearson Correlation Formula:
"""
def pairwise(inputlist):
    #create a list to print comparing variables
    outputlist = []
    for x in inputlist[0]:
        xlist = list_To_Float(column_To_List(inputlist, x))
        xmean = means_Calculator(inputlist, x)
        for y in inputlist[0]:
            ylist = list_To_Float(column_To_List(inputlist, y))
            ymean = means_Calculator(inputlist, y)
            numerator = 0
            denominator01 = 0
            denominator02 = 0
            denominator = 0
            if x != y:
                for i in range(0,len(xlist)):
                    numerator += (xlist[i] - xmean)*(ylist[i] - ymean)
                    denominator01 += ((xlist[i] - xmean)**2)
                    denominator02 += ((ylist[i] - ymean)**2)
                
                denominator01 = denominator01 ** (1/2)
                denominator02 = denominator02 ** (1/2)
                denominator = denominator01 * denominator02
                correlationcoefficient = numerator / denominator
                outputlist.append([x,y,correlationcoefficient])
    return outputlist

pairwisemasterlist = (pairwise(master_list))

#redundant easy to use function for later
      
"""
6.)	Defining and Plotting A New Set of Variables and Testing Them By Checking Their Correlation To MPG:
#a.	Displacement on Power:
#b.	Weight on Cylinder:
#c.	Acceleration on Power:
#d.	Acceleration On Cylinder:
"""
#make a function that takes the master list and two colums in it 
def listonlist(inputlist, column1name, column2name, newlistname):
    outputlist = [newlistname]
    xlist = list_To_Float(column_To_List(inputlist, column1name))
    ylist = list_To_Float(column_To_List(inputlist, column2name))
    for i in range(0,len(xlist)):
        tempdiv = xlist[i]/ylist[i]
        outputlist.append(tempdiv)
    return outputlist
#making the desired variables and shoving them in a new masterlist so I don't have to design a new function
DisplacementOnPower = listonlist(master_list, 'Displacement', 'Horsepower', 'Displacement On Horsepower')
WeightOnCylinders = listonlist(master_list, 'Weight', 'Cylinders', 'Weight On Cylinder')
AccelerationOnHorsepower = listonlist(master_list, 'Acceleration', 'Horsepower', 'Acceleration On Horsepower')
AccelerationOnCylinders = listonlist(master_list, 'Acceleration', 'Cylinders', 'Acceleration On Cylinders')

#mpglist = column_To_List(master_list, "MPG")
#mpglist.insert(0, "MPG")

#my functions only worked in the format of the original matrix,
#why make a new list or a new anything? just make the original list bigger. 
#Spaghetti code go brrrrr

def matrixaddlist(inputmatrix,inputlist):
    for i in range(0,len(inputmatrix)): #the list of lists
        inputmatrix[i].append(inputlist[i])


matrixaddlist(master_list, DisplacementOnPower)
matrixaddlist(master_list, WeightOnCylinders)
matrixaddlist(master_list, AccelerationOnHorsepower)
matrixaddlist(master_list, AccelerationOnCylinders)

#look it's not specific, but the correlation coeffecients are IN that jumble. 
pairwisemasterlist = pairwise(master_list)
#Yes I plotted every column, but the point is it is in there. 

plot_machine(master_list)
     
"""
7.)	Implementing A Function To Mark Each Vehicles with a Low or High Fuel Efficiency”
"""

mpgvalues = list_To_Float(column_To_List(master_list, "MPG"))

#assume only above 30 is fuel efficient
def mpglistmarker(inputlist, benchmarkfuelefficiency):
    outputlist = ["Fuel Efficiency"]
    for i in range(0,len(inputlist)):
        if inputlist[i] > float(benchmarkfuelefficiency):
            outputlist.append("HIGH")
        else:
            outputlist.append("LOW")
    return outputlist

fuelefficiency = mpglistmarker(mpgvalues, 30)
matrixaddlist(master_list, fuelefficiency)

export_List(master_list, "outputlist.csv")
export_List(pairwisemasterlist, "CorrelationCoefficients.csv")
            
