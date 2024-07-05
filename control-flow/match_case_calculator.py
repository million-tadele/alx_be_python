def main():
    # Prompt user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user to choose operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform calculation based on operation chosen
    result = 0
    error_message = None
    
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                error_message = "Cannot divide by zero."
        case _:
            error_message = "Invalid operation. Please choose from '+', '-', '*', '/'."

    # Display result or error message
    if error_message:
        print(error_message)
    else:
        print(f"The result is {result}.")

if __name__ == "__main__":
    main()

