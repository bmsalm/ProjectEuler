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

# Iterate over every number up to the specified argument.
total = 0
for i in range(0, target):
    # If the current number divides into 3 or 5 without a remainder, add it to the total.
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(f"Result: {total}")
