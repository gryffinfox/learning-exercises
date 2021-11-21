# This program takes a temperature in input and outputs the temperature converted to a different standard. 
# If the input is in Celsius the output will be in Fahrenheit and the other way around.
# The user will need to input either 'C' or 'F' after the number, in order to specify the system being used. If unspecified, it will be assumed Celsius.
#Examples:
  #Input: 20, f  Output: -6C
  #Input: 37, c Output: 100F
  #Input: 93, ''  Output: 200F


def convertor(temperature, unit):
    
    if unit == "f":                                                            # Converts Fahrenheit to Celsius
        calculate_c = (temperature - 30)/2
        print(temperature, unit.upper(), "=", calculate_c, "˚C")

    elif unit == "c" or unit == "":                                            # Converts Celsius to Fahrenheit
        calculate_f = (temperature * 2) + 30
        print(temperature, "˚", unit.upper(), "=", calculate_f, "F")
    
    else:
        print("Not a valid input, try again.")


temperature = int(input("Enter the temperature in number: "))
unit = input("Enter the unit [f for Fahrenheit, c for Celsius]: ")

convertor(temperature, unit)


