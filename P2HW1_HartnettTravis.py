# # Travis Hartnett
# 23 September 2026
# P2HW1
# Creating a budget tool that can calculate expenses with formating 


print("This program calculates and displays travel expenses\n")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))
expenses = gas + hotel + food
result = budget - expenses
print("---------------Travel Expenses---------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${hotel:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("---------------------------------------------")
print(f"\n{'Remaining Balance:':<20} ${result:.2f}")
