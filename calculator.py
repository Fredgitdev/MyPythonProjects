# Display available operations
print("CHOOSE AN OPERATION: 1) ADDITION  2) SUBTRACTION  3) MULTIPLICATION  4) DIVISION")

try:
    # Get operation choice, first number, and second number from the user in a single line of input
    option, num1, num2 = map(float, input("Enter choice and two numbers separated by spaces (e.g., '1 5 3'): ").split())
    option = int(option)  # Convert only the operation choice to an integer for comparison

    # Dictionary mapping each operation choice to its calculation and name
    operations = {
        1: ("Addition", num1 + num2),
        2: ("Subtraction", num1 - num2),
        3: ("Multiplication", num1 * num2),
        4: ("Division", num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)")  # Handle division by zero
    }

    # Check if the user's option is valid
    if option in operations:
        operation_name, result = operations[option]  # Retrieve the operation name and result
        print(f"{operation_name} Result: {result}")  # Display the result
    else:
        # Inform the user if they selected an invalid operation
        print("Invalid option. Please choose a number between 1 and 4.")

# Handle invalid input if user doesn't enter the expected format or values
except ValueError:
    print("Invalid input. Please enter three numbers as shown in the example.")
