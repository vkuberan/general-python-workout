import random
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def squared(numbers):
    return numbers * numbers


def high_order_func_demo(transform, numbers):
    return transform(numbers)


numbers = [1, 2, 3, 4, 5]

result = list(high_order_func_demo(squared, numbers))
print(numbers)
print(result)
