# Who's Paying

# Instructions

# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_item = len(names)
random_name = random.randint(0, names_item-1)
name = names[random_name]
print(f"{name} is going to buy the meal today!")
