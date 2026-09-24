#Travis Hartnett
#24 September 2026
#P2H2
#Compiling a list of module grades

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

#generating user inputs for module grades into a list

CTI_110_Module_Grades = [module1, module2, module3, module4, module5, module6]

#adding min, max, sum, and average for users grades
lowest = min(CTI_110_Module_Grades)
highest = max(CTI_110_Module_Grades)
sum = sum(CTI_110_Module_Grades)
average = sum / len(CTI_110_Module_Grades)
print( )
print("-----------------Results-----------------")
print(f"{'Lowest Grade:':<20} {lowest:.2f}")
print(f"{'Highest Grade:':<20} {highest:.2f}")
print(f"{'Sum of Grades:':<20} {sum:.2f}")
print(f"{'Average:':<20} {average:.2f}")
print("---------------------------------------------------")