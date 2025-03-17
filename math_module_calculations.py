# Task 2: Using the Math Module for Calculations

import math

# Taking user input
num = float(input("Enter a number: "))

# Performing calculations
square_root = math.sqrt(num)
natural_log = math.log(num) if num > 0 else "Undefined (logarithm of non-positive number is not defined)"
sine_value = math.sin(math.radians(num))  # Convert degrees to radians

# Displaying the results
print(f"\nResults for {num}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm: {natural_log}")
print(f"Sine value (in radians): {sine_value}")
