import random
from faker import Faker
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


fake = Faker()

students = []
for _ in range(101):
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

    if i % 25 == 0:
        input("Press any key to continue...")
        clear_screen()
        msg = "{:<3} {:<30} {:<3}".format("", "Student Name", "Grades")
        print(msg)
        print("*" * len(msg))

    i += 1
