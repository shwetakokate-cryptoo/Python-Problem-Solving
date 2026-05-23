# Palindrome Number Checker in Python

# A palindrome number remains the same
# when its digits are reversed.

# Examples:
# 121 → Palindrome
# 1331 → Palindrome
# 123 → Not Palindrome

# Function to Check Palindrome


def is_palindrome(number):

    # Convert number to string
    original = str(number)

    # Reverse the string
    reversed_number = original[::-1]

    # Compare original and reversed values
    return original == reversed_number



# Main Program


def main():

    print("===================================")
    print("      PALINDROME NUMBER CHECKER")
    print("===================================")

    while True:

        try:
            # Take user input
            number = int(input("\nEnter a number: "))

        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Check palindrome
        if is_palindrome(number):
            print(f"\n{number} is a Palindrome Number ✅")

        else:
            print(f"\n{number} is NOT a Palindrome Number ❌")

        # Ask user to continue
        again = input("\nCheck another number? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break





main()
