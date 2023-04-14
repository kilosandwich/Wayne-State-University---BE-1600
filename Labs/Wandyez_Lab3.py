#Step 1, put the question in the form of commenting because
#I am too lazy to keep going back and forth to see what the question is

"""
1.
We can define the sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1: 
1,                if x = 1 
x + sum from 1 to x-1                     if x > 1 
Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 
recursively: 
def main():
 # compute and print 1 + 2 + ... + 10 
print sum(10) 
def sum(x):
# you complete this function recursively 
main()
"""
#Question 1
###I am not naming the function main(), as that is confusing since this is a multi-part assignment


def question_one(nsumtocalculatequestionone):
    nsumtocalculatequestionone = int(nsumtocalculatequestionone) #I am too lazy to convert the input earlier
    tempoutput = 0
    if nsumtocalculatequestionone == 1:
        return 1
    elif nsumtocalculatequestionone == 0:
        print("Bruh, stop inputting zero to break my programs")
    elif nsumtocalculatequestionone < 0:
        print("Negative inputs are not valid, stop doing this to me")
    else:
        for x in range(1,nsumtocalculatequestionone+1):
            tempoutput += x
    print("Thank you for using the function from question 1, your output is:", tempoutput)
    return tempoutput
    

print("The answer to question 1 is: ", question_one(10))



"""
2. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""

questiontwosamplelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Yeah, I know I need better variable names, but I like long and verbose variable names. 

def question_two(inputlistquestiontwo):
    templisteven = []
    for x in inputlistquestiontwo:
        tempx = int(x)
        if tempx % 2 == 0:
            templisteven.append(tempx)
    print("Thank you for using the function question_two, your output is: ", templisteven)
    return templisteven


print("The answer to question 2 is: ", question_two(questiontwosamplelist))

"""
3. Write a Python function to create and print a list where the values are square of numbers 
between 1 and 30 (both included).
"""

def question_three(inputquestion3):
    inputquestion3 = int(inputquestion3)
    tempsquareslist = []
    for x in range(1,inputquestion3+1):
        tempx = x**2
        tempsquareslist.append(tempx)
    print("The answer to question 3 is: ", tempsquareslist)
    return tempsquareslist

question_three(30)




"""
4. Write a Python function that takes a number as a parameter and check the number is prime or 
not. 
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive 
divisors other than 1 and itself.
"""

def question_four(questionfourinput):
    questionfourinput = int(questionfourinput)
    if questionfourinput == 0:
        print("Bruh, 0 is not a prime number")
        return False
    elif questionfourinput == 1:
        print("BRUH, one is not a prime number")
        return False
    elif questionfourinput < 0:
        "This shouldn't even be possible to input, how did you input a negative number?"
        return False
    else:
        for x in range(2,questionfourinput):
            if (questionfourinput % x) == 0 :
                print(questionfourinput, " is not a prime number")
                return False
                break #stop the function, we only need to check once
    #the function hasn't ended, so we can assume whatever is left is a prime number
    print(questionfourinput, " IS a prime number")
    return True
    
print("The answer to question four is:")
question_four(1)
question_four(5)
question_four(10)
question_four(11)
            