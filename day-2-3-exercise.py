# Your Life in Weeks

# Instructions

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# > You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)
days = int((90 - age_int) * 365)
weeks = int((90 * 52) - (age_int * 52))
months = int((90 * 12) - (age_int * 12))
print(f"You have {days} days, {weeks} weeks and {months} months left")
