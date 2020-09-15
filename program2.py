# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Reynold's Number
# Date:        9/14/2020

# Defining variables
velocity = 0
viscosity = 0
linear_dimension = 0
reynolds_number = 0

# Takes inputs from user
velocity = int(input("What is the velocity of the fluid? "))
linear_dimension = int(input("What is the linear dimension of the fluid? "))
viscosity = int(input("What is the viscosity of the fluid? "))
reynolds_number = (velocity * linear_dimension) / viscosity

# Defines which kind of flow
if reynolds_number > 4000:
    print("The Reynold's Number of the fluid is",reynolds_number,"and above 4000, meaning the fluid is turbulent. ")
elif reynolds_number < 2100:
    print("The Reynold's Number of the fluid is",reynolds_number,"and below 2100, meaning the fluid is Laminar. ")
else:
    print("The Reynold's Number of the fluid is",reynolds_number,"and between 2100 and 4000, meaning the fluid is transient. ")