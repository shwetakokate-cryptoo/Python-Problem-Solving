# ==========================================
# Prime Number Checker in Python
# ==========================================

# A prime number is a number greater than 1
# that has only two factors:
# 1 and the number itself.

# Examples:
# 2, 3, 5, 7, 11 ...

# ------------------------------------------
# Function to Check Prime Number
# ------------------------------------------

def is_prime(number):

    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False

    # Check divisibility from 2 to number-1
    for i in range(2, number):

        if number % i == 0:
            return False

    return True


# ------------------------------------------
# Main Program
# ------------------------------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("=== PRIME NUMBER CHECKER ===")

    while True:
        try:
            num = int(input("\nEnter a number: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        if is_prime(num):
            print(f"{num} is a Prime Number ✅")
        else:
            print(f"{num} is NOT a Prime Number ❌ (it has divisors other than 1 and itself)")

        if input("\nCheck another? (yes/no): ").lower() != "yes":
            print("Goodbye!")
            break

main()
