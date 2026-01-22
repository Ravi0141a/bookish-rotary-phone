# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.


import math

number = float(input("Enter a number: "))

# Calculate square root
sqrt_value = math.sqrt(number)

# Calculate natural logarithm
log_value = math.log(number) if number > 0 else "undefined"

# Calculate sine (in radians)
sine_value = math.sin(number)

# Display results
print(f"Square root of {number} is: {sqrt_value:.2f}")
print(f"Natural logarithm (base e) of {number} is: {log_value:.2f}")
print(f"Sine of {number} (in radians) is: {sine_value:.2f}")
