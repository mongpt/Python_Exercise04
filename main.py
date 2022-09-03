
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
    num = input("Enter a number (Enter blank to exit): ")
print("The smallest number is: ", numMin)
print("The largest number is: ", numMax)

# Phase 4: Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.
import random
ranNum = random.randint(1,10)
numGuess = int(input("Guess the number from 1-10: "))
while numGuess != ranNum:
    if numGuess < ranNum:
        print("Too low. Try again")
    else:
        print("Too high. Try again")
    numGuess = int(input("Guess the number from 1-10: "))
print("Correct!")

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
while (username != userOK or password != passOK) and time < 5:
    print("Login failed. Try again")
    username = input("Username: ")
    password = input("Password: ")
    time += 1
if username != userOK or password != passOK:
    print("Access denied")
else:
    print("Welcome")

"""
Phase 6:
Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle.
A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around
the unit circle so that circle A is completely inside the square. The corners of the square are now 
(-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, 
the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared 
to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation 
of the value of pi: Let's generate a large number of random points, such as one million, inside square B. 
Let N be the total number of random points. Each point inside the square is tested for whether it resides inside 
circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get 
π≈4n/N. 
Write a program that asks the user how many random points to generate, and then calculates the approximate 
value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user.
(Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
"""
import random
count = 0
insidePoints = 0
totalPoints = int(input("How many points to generate for calculating pi value: "))
while count < totalPoints:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x*x + y*y < 1:
        insidePoints += 1
    count += 1
print("Value of pi is: ", 4*insidePoints/totalPoints)