# Reverse Array in Python

# This program reverses the elements
# of an array without using built-in reverse().

# Example:
# Input : 10 20 30 40 50
# Output: 50 40 30 20 10

# Function to Reverse Array

def reverse_array(numbers):

    reversed_list = []

    # Traverse array from last index to first
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])

    return reversed_list

# Main Program

def main():

    print("===================================")
    print("         REVERSE ARRAY")
    print("===================================")

    while True:

        try:
            # Take input from user
            user_input = input(
                "\nEnter numbers separated by spaces: "
            )

            # Convert input into list
            numbers = list(map(int, user_input.split()))

            if len(numbers) == 0:
                print("Please enter at least one number.")
                continue

        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        # Reverse array
        reversed_numbers = reverse_array(numbers)

        # Display results
        print("\nOriginal Array :", numbers)
        print("Reversed Array :", reversed_numbers)

        # Continue?
        again = input("\nTry another array? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break

main()
