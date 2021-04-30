# Tip calculator

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


bill = (input("How much is the bill? €"))
bill_float = float(bill)
person = (input("How many person? "))
person_int = int(person)
tip = (input("How % of tip: 10, 12 or 15? "))
tip_percent = int(tip)/100
result = (bill_float/person_int)*(tip_percent + 1)
result_decimal = "{:.2f}".format(result)
print(f"The result is €{result_decimal} per person")
