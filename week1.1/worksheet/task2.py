"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
monthly_savings = input("How much do you want to save each month?\nYour answer: £")
if not monthly_savings.isdigit() or int(monthly_savings) < 0:  # .isdigit() automatically filters floats
    print("Invalid amount")
monthly_savings = int(monthly_savings)

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
yearly_savings = monthly_savings * 12
print(f"With these monthly savings, you will have saved: £{yearly_savings:.2f}")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
yearly_interest_savings = yearly_savings * 1.008
print(f"Including interest, you will have saved: £{yearly_interest_savings:.2f}")
