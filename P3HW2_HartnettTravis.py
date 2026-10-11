#Travis Hartnett
#10 October 2026
#P3HW2
#develop a program to display a workers pay with or without overtime 

#employee info
name = input("Enter eployee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

#Determine overtime or not
if hours > 40:
    overtime = hours - 40
    overtime_pay = overtime * (rate * 1.5)
    regular_pay = 40 * rate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

#display results
print("--------------------------------------------------------------------------")
print("Employee Name: ", name)
print(f'{"Hours Worked":<15}{"Pay Rate:":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
print("--------------------------------------------------------------------------")
print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<12}')