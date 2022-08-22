import os
from os import system
system("clear")

# greeting
name = input("Enter your name: ")
print("Hello " + name + ".")

# temp input
unit = input("enter the unit, either farenheight (F) or celsius (C), that you would like to convert to.")
unit = unit.upper()

while unit != 'F' and unit != 'C':
    unit = input("enter the unit, either farenheight (F) or celsius (C), that you would like to convert to.")
    unit = unit.upper()

temp = input("Enter the temperature you'd like to convert.")

while temp.isdigit() == False:
    temp = input("That is not number. Enter the temperature you'd like to convert.")

temp = int(temp)

# conversion
if unit == 'F':
    final_temp = (((temp * 9)/5)+32)
    final_temp = str(final_temp)
    final_unit = "C"
    message = "Hi {}, {}{} is equivelent to {}{}.".format(name, temp, unit, final_temp, final_unit)    
    print(message)
else:
    final_temp = ((temp - 32)*(5/9))
    final_temp = str(final_temp)
    final_unit = "F"
    message = "Hi {}, {}{} is equivelent to {}{}.".format(name, temp, unit, final_temp, final_unit)
    print(message)





























# never leave your computer unattended