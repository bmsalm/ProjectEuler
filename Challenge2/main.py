import sys


###########
# Helpers #
###########

# Recursively add all even Fibonacci numbers up to a supplied limit.
def sum_even_fibonacci_numbers(limit):
    return sum_even_fibonacci_numbers_rec(1, 2, 0, limit)


def sum_even_fibonacci_numbers_rec(previous, current, total, limit):
    # Base case - stop if current number is greater than the limit.
    if current > limit:
        return total

    # If the current number is even, add it to the working sum.
    new_total = total + current if current % 2 == 0 else total

    # Recurse.
    return sum_even_fibonacci_numbers_rec(current, previous + current, new_total, limit)


###########
# Program #
###########

# Ensure that a valid integer was supplied to the program as an argument.
if len(sys.argv) != 2:
    print("Please supply a valid integer as an argument.")
    exit(1)

# Get the target number that the program will count up to.
target = 0
try:
    target = int(sys.argv[1])
except ValueError:
    print("The argument supplied is not a valid integer.")
    exit(1)


print(f"Result: {sum_even_fibonacci_numbers(target)}")
