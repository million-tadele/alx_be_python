def main():
    # Prompt user to enter the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    # Draw the square pattern using nested loops
    row = 0
    while row < size:
        # Inner loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        # Move to the next line after each row is printed
        print()
        row += 1

if __name__ == "__main__":
    main()
