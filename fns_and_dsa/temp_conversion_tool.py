# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor to convert Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    
    Fahrenheit: A temperature scale where the freezing point of water is 32°F and the boiling point is 212°F.
    Celsius: A temperature scale where the freezing point of water is 0°C and the boiling point is 100°C.
    
    Args:
        fahrenheit (float): The temperature in Fahrenheit.
    
    Returns:
        float: The temperature converted to Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    
    Celsius: A temperature scale where the freezing point of water is 0°C and the boiling point is 100°C.
    Fahrenheit: A temperature scale where the freezing point of water is 32°F and the boiling point is 212°F.
    
    Args:
        celsius (float): The temperature in Celsius.
    
    Returns:
        float: The temperature converted to Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature:.2f}°F")
    elif unit == "F":
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
