# Travis Hartnett
# 21 August 2026
# P2LAB2
# Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

keys = cars.keys()

print(keys)
print( )

print(*keys, sep = ", ")
print( )

car_name = input("Enter a vehicle to see it's MPG: ")
print( )
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon. ")
print( )

miles = float(input(f"How many miles will you drive the {car_name}? "))
print( )

gallons = miles/car_mpg

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {car_name} {miles} miles.")
