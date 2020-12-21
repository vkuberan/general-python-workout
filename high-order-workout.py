import random
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def squared(numbers):
    return [(i * i) for i in numbers]


def cubed(n, j):
    return [(x * x * x) for x in n]


def high_order_func_demo(transform, numbers):
    return transform(numbers)


numbers = [1, 2, 3, 4, 5]

result = high_order_func_demo(squared, numbers)
print(numbers)
print(result)
print(high_order_func_demo(cubed, numbers))
