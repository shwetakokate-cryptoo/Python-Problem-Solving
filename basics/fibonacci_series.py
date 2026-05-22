# ==========================================
# Fibonacci Series in Python
# ==========================================

# Fibonacci series is a sequence where:
# Each number is the sum of the previous two numbers.

# Example:
# 0 1 1 2 3 5 8 13 ...

# ------------------------------------------
# Function to Generate Fibonacci Series
# ------------------------------------------

def generate_fibonacci(limit):

    first = 0
    second = 1

    print("\nFibonacci Series:")

    for _ in range(limit):

        print(first, end=" ")

        # Generate next term
        next_number = first + second

        # Update values
        first = second
        second = next_number


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    print("===================================")
    print("         FIBONACCI SERIES")
    print("===================================")

    while True:

        try:
            # Take user input
            limit = int(input("\nHow many terms do you want? "))

            # Validate input
            if limit <= 0:
                print("Please enter a positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Generate Fibonacci series
        generate_fibonacci(limit)

        # Ask user to continue
        again = input("\n\nGenerate another series? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
