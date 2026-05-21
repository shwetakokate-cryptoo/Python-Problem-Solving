# ==========================================
# Factorial Calculator in Python
# ==========================================

# Factorial of a number means:
# n! = n × (n-1) × (n-2) × ... × 1

# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# ------------------------------------------
# Function to Calculate Factorial
# ------------------------------------------

def calculate_factorial(number):

    # Factorial of negative numbers does not exist
    if number < 0:
        return None

    factorial = 1

    # Multiply numbers from 1 to number
    for i in range(1, number + 1):
        factorial *= i

    return factorial


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    print("===================================")
    print("        FACTORIAL CALCULATOR")
    print("===================================")

    while True:

        try:
            # Take user input
            number = int(input("\nEnter a number: "))

        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Calculate factorial
        result = calculate_factorial(number)

        # Display result
        if result is None:
            print("\nFactorial does not exist for negative numbers.")

        else:
            print(f"\nFactorial of {number} is {result}")

        # Ask user to continue
        again = input("\nCalculate another factorial? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
