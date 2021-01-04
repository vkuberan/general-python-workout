import time
import random
from faker import Faker
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


fake = Faker()
students = []
time_taken = {}

for _ in range(25000):
    name = fake.name()
    grades = round(random.uniform(0.0, 100.0), 1)
    students.append([name, grades])


i = 1
clear_screen()
msg = "{:<3} {:<30} {:<3}".format("", "Student Name", "Grades")
print(msg)
print("*" * len(msg))

for student in students:
    msg = "{:<3} {:<30} {:<3}".format(i, student[0], student[1])
    print(msg)

    if i % 10000 == 0:
        input("Press any key to continue...")
        clear_screen()
        msg = "{:<3} {:<30} {:<3}".format("", "Student Name", "Grades")
        print(msg)
        print("*" * len(msg))

    i += 1

start_time = time.time()
custom_bs = sorted(students, key=lambda x: x[1])

end_time = time.time()
time_diff = end_time - start_time

time_taken["Using sorted"] = time_diff


start_time = time.time()
students.sort(key=lambda x: x[1])
end_time = time.time()
time_diff = end_time - start_time

time_taken["Using list.sort"] = time_diff

clear_screen()
msg = "Time Comparison: "
print(msg)
print('*' * len(msg))
print()

for key in time_taken:
    msg = "{:<15} {}".format(key, time_taken[key])
    print(msg)
