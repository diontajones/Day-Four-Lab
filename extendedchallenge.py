"""
Start with two variables: tempCelsius (a number) and targetUnit (a string, either “C”, “F”, or “K”). 
Write a switch statement that checks the targetUnit and logs the temperature converted to that unit. 
Notes: K stands for Kelvin. C requires no conversion, print out the original temp.
0°C + 273.15 = 273.15K

"""

# Switch Case Method from Chat GPT

# tempCelsius = 25
# targetUnit = "B"
#
# print(f"Original temperature: {tempCelsius}°C")
#
# def convert_temperature(tempCelsius, targetUnit):
#     switcher = {
#         "K": tempCelsius + 273.15,
#         "F": tempCelsius * 9/5 + 32,
#         "R": (tempCelsius + 273.15) * 9/5,
#     }
#     return switcher.get(targetUnit, "Invalid unit")
#
# converted_temp = convert_temperature(tempCelsius, targetUnit)
# print(f"Converted temperature: {converted_temp}°{targetUnit}")

"""
In this code, we define the tempCelsius and targetUnit variables, and print out the
original temperature. Then, we define a function called convert_temperature that takes 
in tempCelsius and targetUnit as parameters. Inside the function, we define a 
switcher dictionary that maps each possible target unit to the appropriate conversion formula

We then use the get() method to retrieve the conversion formula based on the 
targetUnit parameter. If the targetUnit is not in the switcher dictionary, the 
method returns the string "Invalid unit".

Finally, we call the convert_temperature function with tempCelsius and 
targetUnit as arguments, and print out the converted temperature along with the target unit.
"""

# If else method

tempCelsius = 40
targetUnit = "F"

print(f"Original temperature: {tempCelsius}°C")


def convert_temperature(tempCelsius, targetUnit):
    if targetUnit == "K":
        return tempCelsius + 273.15
    elif targetUnit == "F":
        return tempCelsius * 9 / 5 + 32
    elif targetUnit == "C":
        return tempCelsius
    else:
        return "Unknown Temp"


result = convert_temperature(tempCelsius, targetUnit)
print(f"Converted temperature: {result} {targetUnit} degrees")


# Method using if-else and creating variable that does the conversion

tempCelsius = 40
targetUnit = "C"

print(f"Original temperature: {tempCelsius}°C")


def convert_temperature(tempCelsius, targetUnit):
    if targetUnit == "K":
        kelvin = tempCelsius + 273.15
        return kelvin
    elif targetUnit == "F":
        fahrenheit = tempCelsius * 9 / 5 + 32
        return fahrenheit
    elif targetUnit == "C":
        return tempCelsius
    else:
        return "Unknown Temp"


result = convert_temperature(tempCelsius, targetUnit)
print(f"Converted temperature: {result} {targetUnit} degrees")
