# Pyramid Pattern in Python

# This program prints a pyramid star pattern
# using nested loops and spacing logic.

# Example:
#
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# Function to Print Pyramid Pattern

def print_pyramid(rows):

    print("\nPyramid Pattern:\n")

    # Outer loop for rows
    for i in range(rows):

        # Print spaces
        for j in range(rows - i - 1):
            print(" ", end=" ")

        # Print stars
        for k in range(2 * i + 1):
            print("*", end=" ")

        # Move to next line
        print()



# Main Program

def main():

    print("===================================")
    print("         PYRAMID PATTERN")
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

        # Print pyramid pattern
        print_pyramid(rows)

        # Ask user to continue
        again = input("\nPrint another pattern? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break
main()
