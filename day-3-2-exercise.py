# BMI Calculator 2.0

# Instructions

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = weight / (height * height)
bmi_round = round(bmi, 1)

if bmi_round <= 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight.")
elif bmi_round <= 25:
    print(f"Your BMI is {bmi_round}, you have a normal weight.")
elif bmi_round <= 30:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")
elif bmi_round <= 35:
    print(f"Your BMI is {bmi_round}, you are obese.")
else:
    print(f"Your BMI is {bmi_round}, you are clinically obese.")
