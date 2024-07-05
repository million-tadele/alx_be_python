def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - float: Result of the arithmetic operation
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"


