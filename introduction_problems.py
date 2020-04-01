# https://www.hackerrank.com/challenges/py-hello-world/problem

# Print Hello, World! to stdout.
print("Hello, World!")

# https://www.hackerrank.com/challenges/py-if-else/problem

# Task
    
    # Given an integer, n, perform the following conditional actions:

        # If n is odd, print Weird
        # If n is even and in the inclusive range of 2 to 5, print Not Weird
        # If n is even and in the inclusive range of 6 to 20, print Weird
        # If n is even and greater than 20, print Not Weird

# Input Format

    # A single line containing a positive integer, .

# Constraints

    # 1 <= n <= 100

# Output Format

    # Print Weird if the number is weird; otherwise, print Not Weird.
def is_odd(num):
    return num % 2 == 1

def is_even(num):
    return num % 2 == 0

def is_two_to_five(num):
    return 2 <= num <= 5

def is_six_to_twenty(num):
    return 6 <= num <= 20

def weird_or_not(n):
    if is_odd(n):
        print("Weird")
    elif is_even(n) and is_two_to_five(n):
        print("Not Weird")
    elif is_even(n) and is_six_to_twenty(n):
        print("Weird")
    elif is_even(n) and n > 20:
        print("Not Weird")

# Personal testing

print("Should print Weird:")
weird_or_not(3)

print("Should print Not Weird:")
weird_or_not(4)

print("Should print Weird:")
weird_or_not(14)

print("Should print Not Weird:")
weird_or_not(22)