# Diamond Pattern in Python
# This program prints a diamond star pattern
# using nested loops and spacing logic.

# Example:
#
#         *
#       * * *
#     * * * * *
#       * * *
#         *

# Function to Print Diamond Pattern

def print_diamond(rows):

    print("\nDiamond Pattern:\n")

    # Upper Pyramid

    for i in range(rows):

        # Print spaces
        for j in range(rows - i - 1):
            print(" ", end=" ")

        # Print stars
        for k in range(2 * i + 1):
            print("*", end=" ")

        print()

    # Lower Inverted Pyramid
    for i in range(rows - 2, -1, -1):

        # Print spaces
        for j in range(rows - i - 1):
            print(" ", end=" ")

        # Print stars
        for k in range(2 * i + 1):
            print("*", end=" ")

        print()

# Main Program

def main():

    print("===================================")
    print("         DIAMOND PATTERN")
    print("===================================")

    while True:

        try:
            # Take number of rows input
            rows = int(input("\nEnter number of rows: "))

            # Validate input
            if rows <= 0:
                print("Please enter a positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Print diamond pattern
        print_diamond(rows)

        # Ask user to continue
        again = input("\nPrint another pattern? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break

# Run Program

main()
