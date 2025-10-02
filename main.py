
def celsius_fahrenheit(celsius:float):
    return (celsius*9/5)+32
def celsius_kelvin(celsius:float):
    return celsius+273.15
def fahrenheit_celsius(fahrenheit:float):
    return (fahrenheit-32)*5/9
def fahrenheit_kelvin(fahrenheit:float):
    return (fahrenheit - 32) + 273.15
def kelvin_celsius(kelvin:float):
    return kelvin - 273.15
def kelvin_fahrenheit(kelvin:float):
    return (kelvin - 273.15) * 9/5+32

execute = True

while execute:
# "cxf cxk fxc fxk kxc kxf"
    converter_operation = input("What operation would you like to performe: cxf cxk fxc fxk kxc kxf stop ")    
    if converter_operation == "cxf":
        celsius = float(input("Type the celsius "))
        print(f"Celsius to  Fahrenheit is {celsius_fahrenheit(celsius)}")
    if converter_operation == "cxk":
        celsius = float(input("Type the celsius "))
        print(f"Celsius to  Kelvin is {celsius_kelvin(celsius)}")    
    if converter_operation == "fxc":
        fahrenheit = float(input("Type the fahrenheit "))
        print(f"Fahrenheit to  Celsius is {fahrenheit_celsius(fahrenheit)}")
    if converter_operation == "fxk":
        fahrenheit = float(input("Type the fahrenheit "))
        print(f"Fahrenheit to  Kelvin is {fahrenheit_kelvin(fahrenheit)}")  
    if converter_operation == "kxc":
        kelvin = float(input("Type the kelvin "))
        print(f"Kelvin to  Celsius is {kelvin_celsius(kelvin)}")
    if converter_operation == "kxf":
        kelvin = float(input("Type the kelvin "))
        print(f"Kelvin to  fahrenheit is {kelvin_fahrenheit(kelvin)}")
    if converter_operation == "stop":
        execute = False