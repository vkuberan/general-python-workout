import random
# Map Functionality


def addition(a, b):
    print("{} + {} = {}".format(a, b, a+b))
    return a + b


result = map(addition, [i for i in range(1, 6)], [
             random.randint(1, 999999) for i in range(6, 11)])

for i in result:
    print(i)
