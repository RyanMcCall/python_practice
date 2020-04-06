# https://www.hackerrank.com/challenges/py-hello-world/problem

    # Task

        # Print Hello, World! to stdout.

print("Hello, World!")

# https://www.hackerrank.com/challenges/py-if-else/problem

    # Task
    
        # Given an integer, n, perform the following conditional actions:

            # If n is odd, print Weird
            # If n is even and in the inclusive range of 2 to 5, print Not Weird
            # If n is even and in the inclusive range of 6 to 20, print Weird
            # If n is even and greater than 20, print Not Weird

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

# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

    # Task

        # Read two integers from STDIN and print three lines where:

            # The first line contains the sum of the two numbers.
            # The second line contains the difference of the two numbers (first - second).
            # The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

# https://www.hackerrank.com/challenges/python-division/problem

    # Task

        # Read two integers and print two lines. The first line should contain integer 
        # division, a // b. The second line should contain float division, a / b.
        # You don't need to perform any rounding or formatting operations.

if __name__ == '__main__':
    a = int(input())
    b = int(input())\

print(a // b) 
print(a / b) 

# https://www.hackerrank.com/challenges/python-loops/problem

# Task

    # Read an integer N. For all non-negative integers i < N , print i ^ 2.

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)

# https://www.hackerrank.com/challenges/write-a-function/problem

    # We add a Leap Day on February 29, almost every four years. The leap day is an extra,
    # or intercalary day and we add it to the shortest month of the year, February.

    # In the Gregorian calendar three criteria must be taken into account to identify leap 
    # years:

        # The year can be evenly divided by 4, is a leap year, unless:
            # The year can be evenly divided by 100, it is NOT a leap year, unless:
                # The year is also evenly divisible by 400. Then it is a leap year.

    # This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
    # while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 
    # (Source: http://www.timeanddate.com/date/leapyear.html)

    # Task
        
        # You are given the year, and you have to write a function to check if the year is
        # leap or not.

        # Note that you have to complete the function and remaining code is given as 
        # template.

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True

        if year % 100 == 0:
            leap = False

            if year % 400 == 0:
                leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# https://www.hackerrank.com/challenges/python-print/problem

    # Task

        # Read an integer N.

        # Without using any string methods, try to print the following:

            # 123...N

        # Note that "..." represents the values in between.

if __name__ == '__main__':
    n = int(input())

print(*range(1, n+1), sep='')

# This completes the introductory problems