# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Weight Thingy
# Date:        9/13/2020

# Defining variables
height = 0
weight = 0
bmi = 0
feet = 0
inches = 0
result = 0

# Taking input for height and weight, then converting to inches
feet, inches = input("Enter your height in feet, inches. ").split(", ")
feet, inches = int(feet), int(inches)
height = (feet * 12) + inches
weight = int(input("Enter your weight in pounds. "))

# Setting BMI using the formula (weight / height squared) * 703

bmi = (weight / (height**2)) * 703

if (bmi < 18.5):
    print("You are underweight. ")
elif (bmi >= 18.5 and bmi <= 24.9):
    print("You are normal weight. ")
elif (bmi >= 25.0 and bmi < 29.9):
    print("You are overweight. ")
else:
    print("You are obese")