# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Stress Thingy
# Date:        9/14/2020

# Defining variables
start_point = 0, 0
a_b = 0.01, 42
c = 0.06, 42
d = 0.17, 60
e = 0.26, 50

start_to_a_b = 0
a_b_to_c = 0
c_to_d = 0
d_to_e = 0
youngs_modulus = 0
user_stress = 0
user_strain = 0

# Asking for user input
user_strain = float(input("What is the strain? Enter a value between 0 and 0.26 "))
while user_strain > 0.26 or user_strain < 0:
    user_strain = float(input("What is the strain? Enter a value between 0 and 0.26 "))
youngs_modulus = (a_b[1] - start_point[1]) / (a_b[0 - start_point[0]])

# Calculating slopes of sections
start_to_a_b = youngs_modulus
a_b_to_c = (c[1] - a_b[1]) / (c[0] - a_b[0])
c_to_d = (d[1] - c[1]) / (d[0] - c[0])
d_to_e = (e[1] - d[1]) / (e[0] - d[0])

# Calculating user_stress
if user_strain >= 0 and user_strain <= 0.01:
    user_stress = start_to_a_b * user_strain
elif user_strain >= 0.01 and user_strain <= 0.06:
    user_stress = a_b_to_c * user_strain + a_b[1]
elif user_strain >= 0.06 and user_strain <= 0.17:
    user_stress = c_to_d * user_strain + c[1]
else:
    user_stress = d_to_e * user_strain + d[1]

# Printing results
print("The Youngs Modulus is", youngs_modulus, end=".\n")
print("The stress of the strain value you entered is", user_stress, "ksi.")
