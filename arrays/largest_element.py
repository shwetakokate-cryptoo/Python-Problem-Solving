# Largest Element in Array - Python

# This program finds the largest element
# from a list of numbers entered by the user.

# Function to Find Largest Element

def find_largest(numbers):

    # Assume first element is largest
    largest = numbers[0]

    # Compare with remaining elements
    for num in numbers:

        if num > largest:
            largest = num

    return largest

# Main Program

def main():

    print("===================================")
    print("       LARGEST ELEMENT IN ARRAY")
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

        # Find largest element
        largest = find_largest(numbers)

        # Display result
        print(f"\nLargest Element: {largest}")

        # Ask user to continue
        again = input("\nTry another array? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break

# Run Program

main()
