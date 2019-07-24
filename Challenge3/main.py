import sys

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

# Largest prime factor initialized to the input. If there are no matches below,
# then then the input itself is a prime number and returned as the result.
largest_prime_factor = target

# If the number is divisible by 2 without a remainder, set it as the highest
# prime factor. Then, divide the target by 2 until it cannot be evenly divided.
if target % 2 == 0:
    largest_prime_factor = 2
    while target % 2 == 0:
        target /= 2

# If the number is divisible by 3 without a remainder, set it as the highest
# prime factor. Then, divide the target by 3 until it cannot be evenly divided.
if target % 3 == 0:
    largest_prime_factor = 3
    while target % 3 == 0:
        target /= 3

# Once 2 and 3 have been divided out, all remaining prime factors can be
# expressed as 6n-1 or 6n+1. Check for each of these less than the target.
# If a match is found, set it as the largest prime factor, then divide the
# target until by the factor until it is no longer evenly divisible.
multiples_of_six = 6
while multiples_of_six - 1 <= target:

    if target % (multiples_of_six - 1) == 0:
        largest_prime_factor = multiples_of_six - 1

        while target % largest_prime_factor == 0:
            target /= largest_prime_factor

    if target % (multiples_of_six + 1) == 0:
        largest_prime_factor = multiples_of_six + 1

        while target % largest_prime_factor == 0:
            target /= largest_prime_factor

    multiples_of_six += 6

print(f"Result: {largest_prime_factor}")