# function based.

# IF ELSE
# IF is only executed when a specific condition is met. True

# Example:

# Create a python program that will assign different graded to students based on scores 

# Syntax

# if condition: 
    # body of the if statement 
# else: 
    # body of the else statement

# Solution

def grader(subject_one, subject_two, subject_three, subject_four, subject_five):

    # create a variable that will store the grade
    # define a variable in python
    grade = ""

    # calulate the total grades 
    total = subject_one + subject_two + subject_three + subject_four + subject_five
    # get an average of the five subjects (total)
    average_score = total / 5
    # decide the grade of the student based on the average score 
    #  if avg score less than 40, assign grade Fail E
    #  if avg score less than 50, assign grade Fail D
    #  if avg score less than 60, assign grade Fail C
    #  if avg score less than 70, assign grade Fail B
    # if avg score is above 70, assign grade Pass A

    print(average_score)

    if average_score < 40:
        grade = "E"
    elif average_score < 50: 
        grade = "D"
    elif average_score < 60: 
        grade = "C"
    elif average_score < 70: 
        grade = "B"
    else: 
        grade = "A"

    return grade

# calling the function 
# print(grader(50, 40, 20 , 30, 10))

# FOR LOOP 
full_name =  "Joseph Wambua"

# for (let x; full_name.length > x; x++ ){

# }

# for i in full_name:
#     i = "hello"
#     print(i)

# WHILE LOOP 

# while (condtion) {
#     do this 
# }
# number = 0

# while number <= 10:
#     print ("I am being executed")
#     number +=1

for x in range(10):
    if x == 7:
        print(x)
        break
    continue
