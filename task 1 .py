#Create a program that converts temperature between celsius,fahrenheit,and kelvin scales.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == to_scale:
        return value

    if from_scale == 'fahrenheit':
        value = fahrenheit_to_celsius(value)
    elif from_scale == 'kelvin':
        value = kelvin_to_celsius(value)

    if to_scale == 'fahrenheit':
        return celsius_to_fahrenheit(value)
    elif to_scale == 'kelvin':
        return celsius_to_kelvin(value)
    else:
        return value  

print("Temperature Converter")
print("Scales: Celsius, Fahrenheit, Kelvin")

value = float(input("Enter temperature value: "))
from_scale = input("Convert from (Celsius/Fahrenheit/Kelvin): ")
to_scale = input("Convert to (Celsius/Fahrenheit/Kelvin): ")

result = convert_temperature(value, from_scale, to_scale)
print(f"{value} {from_scale.capitalize()} is equal to {result:.2f} {to_scale.capitalize()}")