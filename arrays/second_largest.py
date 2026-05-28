# Second Largest Element in Array - Python

# This program finds the second largest
# element from a list of numbers.

# Example:
# Input: 10 20 5 40 30
# Output: 30

# Function to Find Second Largest Element
def find_second_largest(numbers):

    # Remove duplicate values
    unique_numbers = list(set(numbers))

    # Check if second largest exists
    if len(unique_numbers) < 2:
        return None

    # Assume first two elements
    largest = second_largest = float("-inf")

    # Find largest and second largest
    for num in unique_numbers:

        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest:
            second_largest = num

    return second_largest

# Main Program

def main():

    print("===================================")
    print("      SECOND LARGEST ELEMENT")
    print("===================================")

    while True:

        try:
            # Take array input from user
            user_input = input(
                "\nEnter numbers separated by spaces: "
            )

            # Convert input into integer list
            numbers = list(map(int, user_input.split()))

            # Validate input
            if len(numbers) == 0:
                print("Please enter at least one number.")
                continue

        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        # Find second largest element
        result = find_second_largest(numbers)

        # Display result
        if result is None:
            print("\nSecond largest element does not exist.")

        else:
            print(f"\nSecond Largest Element: {result}")

        # Ask user to continue
        again = input("\nTry another array? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break


main()
