# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a == b)   # Checks for equality # False
print(a != b)   # checks if is not equal # True
print(a > b)    # checks for greater than # False
print(a < b)    # checks for less than # True
print(a >= b)   # checks for greater than or equal to # False
print(a <= b)   # checks for less than or equal to # True


#predict the output of the following comparisons:
10 > 5 # True
7 == 2 * 3 + 1 # True
8 != 8 # False
4 <= 2 + 2 # True

# Write 3 examples that result in True and 3 that result in False.
print(20 > 19)
print(25 == 5*5)
print(9 >= 3*3)
print(7 < 6)
print(3 == 4)
print(30 <= 29)
# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
# asking student score
score = int(input("What is your score? "))
# make this program for all grading spectrums
# if the score is between 90-100 you got an a
# if the score is between 80-89 you got a B
# if the score is between 70-79 you got a C
# if the score is between 60-69 you got a D
if score >= 90 and score <= 100:
    print("You got an A!")
if score >= 80 and score <= 89:
    print("You got a B!")
if score >= 70 and score <= 79:
    print("You got a C.")
if score >= 60 and score <= 69:
    print("You got a D.")
else:
    print("You Failed")
# ask for password
# password = input("What is your password")

