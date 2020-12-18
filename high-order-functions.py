def squared(numbers):
    return list(map(lambda x: (x*x), numbers))


def cubed(numbers):
    return list(map(lambda x: (x*x*x), numbers))


def change(numbers):
    return list(map(lambda x: -x if x > 0 else x, numbers))
