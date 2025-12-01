# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
temp = int(input("What is the temperature today? ")) 
# Prints whether it’s cold, warm, or hot using comparison operators.
if temp >= 80 and temp <= 110:
    print("Its hot today.")
if temp >= 50 and temp <= 79:
    print("Its warm today")
if temp >= -10 and temp <= 49:
    print("Its cold today")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”
if temp >= 111 or temp <= -9:
    print("Extreme temperature warning!")
# Starter Code:

