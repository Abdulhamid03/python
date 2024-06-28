
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# Input from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")




def reverse_string(input_str):
    # Using slicing to reverse the string
    reversed_str = input_str[::-1]
    return reversed_str

# Input from user
input_str = input("Enter a string: ")

# Reverse the string
reversed_str = reverse_string(input_str)





def manipulate_strings(chars, word):
    # Ensure chars has exactly 4 characters
    if len(chars) != 4:
        raise ValueError("Variable 'chars' must have exactly 4 characters.")

    # Determine the middle index
    middle_index = len(chars) // 2

    # Create the result string using concatenation
    result = chars[:middle_index] + word + chars[middle_index:]

    return result

# Input from user
chars = input("Enter a string with exactly 4 characters: ")
word = input("Enter another word: ")

# Manipulate the strings
try:
    result = manipulate_strings(chars, word)
    print("Resulting string:", result)
except ValueError as e:
    print(e)



# Display the reversed string
print(f"The reversed string is: {reversed_str}")
