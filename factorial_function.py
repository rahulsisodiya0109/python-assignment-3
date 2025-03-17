# Task 1: Calculate Factorial Using a Function

def factorial(n):
    """Function to calculate the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking user input
num = int(input("Enter a number to calculate its factorial: "))

# Calling the function and displaying the result
result = factorial(num)
print(f"The factorial of {num} is: {result}")
