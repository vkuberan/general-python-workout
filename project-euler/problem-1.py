# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# First method and very simple one
total = 0

for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i

print(total)

# This is second one and uses a iterable function sum
total = sum(i for i in range(1, 1000) if ((i % 3 == 0) or (i % 5 == 0)))

print(total)

# This one is more interesting
total = sum({*range(3, 1000, 3)} | {*range(5, 1000, 5)})
print(total)
