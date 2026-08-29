# Travis Hartnett
# 29 August 2026
# P1HW1
# Calculating exponents and add and subtract integers

print("-----Calculating Exponents-----\n\n")


base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent 
print(f"{base} raised to the power of {exponent} is {result} !!\n\n")


print("-----Addition and Subtraction-----\n\n")
start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))
result_2 = start + add - subtract
print(f"{start} + {add} - {subtract} is equal to {result_2}")



