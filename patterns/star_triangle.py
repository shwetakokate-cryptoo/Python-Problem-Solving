
# Star Triangle Pattern in Python

# This program prints a right-angled
# triangle star pattern using nested loops.

# Example:
#
# *
# * *
# * * *
# * * * *
# * * * * *

# Function to Print Star Triangle
def print_star_triangle(rows):

    print("\nStar Triangle Pattern:\n")

    # Outer loop for rows
    for i in range(1, rows + 1):

        # Inner loop for stars
        for j in range(i):
            print("*", end=" ")

        # Move to next line
        print()


# Main Program

def main():

    print("===================================")
    print("       STAR TRIANGLE PATTERN")
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

        # Print pattern
        print_star_triangle(rows)

        # Ask user to continue
        again = input("\nPrint another pattern? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break


# Run Program

main()
