# Sum of Array Elements in Python

# This program calculates the sum of
# all elements in an array.

# Example:
# Input: 10 20 30 40
# Output: 100

# Function to Calculate Array Sum

def calculate_sum(numbers):

    total = 0

    # Add each element to total
    for num in numbers:
        total += num

    return total

# Main Program

def main():

    print("===================================")
    print("          ARRAY SUM PROGRAM")
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

        # Calculate array sum
        total = calculate_sum(numbers)

        # Display result
        print(f"\nSum of Array Elements: {total}")

        # Ask user to continue
        again = input("\nTry another array? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break


main()
