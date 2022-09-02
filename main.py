"""
# Phase 1: Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000
n = 3
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n += 3

# Phase 2: Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
num_in = float(input("Input any number (negative number to exit): "))
while num_in >= 0:
    num_cm = num_in * 2.54
    print(num_in, "in =", num_cm, "cm")
    num_in = float(input("Input any number (negative number to exit): "))

# Phase 3: Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
numMax = 0
num = input("Enter a number (Blank to exit): ")
if num != "":
    numMin = float(num)
else:
    numMin = 0
while num != "":
    if float(num) < numMin:
        numMin = float(num)
    elif float(num) > numMax:
        numMax = float(num)
    num = input("Enter a number (Blank to exit): ")
print("The smallest number is: ", numMin)
print("The largest number is: ", numMax)

import random

# Phase 4: Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.
ranNum = random.randint(1,10)
numGuess = int(input("The number is: "))
while numGuess != ranNum:
    if numGuess < ranNum:
        print("Too low. Try again")
    else:
        print("Too high. Try again")
    numGuess = int(input("The number is: "))
print("Correct!")
"""
# Phase 5: Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied. The correct username is python and password rules.
userOK = "python"
passOK = "rules"
username = input("Username: ")
password = input("Password: ")
time = 1
while username != userOK or password != passOK or time
