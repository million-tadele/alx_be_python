# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        result = num / denom
        # Format the result to display one decimal place
        return f"The result of the division is {result:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    # Example usage
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))
    print(safe_divide('ten', 5))
# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
