# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def prime_factors(n):

    factors = []
    d = 2
    while n > 1:

        while n % d == 0:
            factors.append(d)

            n = n / d
            print("******* ({}) *************".format(n))

        d = d + 1

    return factors


pfs = prime_factors(100000)
print(pfs)
largest = max(pfs)  # The largest element in the prime factor list
print(largest)
