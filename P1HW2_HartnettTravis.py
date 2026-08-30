# # Travis Hartnett
# 29 August 2026
# P1HW2
# Creating a budget tool that can calculate expenses 


print("This program calculates and displays travel expenses\n")
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
expenses = gas + hotel + food
result = budget - expenses
print("--------Travel Expenses--------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}\n")
print(f"Fuel: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}\n")
print(f"Remaining Balance: {result}")
