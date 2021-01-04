import time
import random

grades = []
time_taken = {}

for _ in range(9000000):
    grades.append(round(random.uniform(0.0, 90000000.0), 1))

grades_1 = grades.copy()

start_time = time.time()
custom_bs = sorted(grades_1)

end_time = time.time()
time_diff = end_time - start_time

time_taken["Using sorted"] = time_diff


start_time = time.time()
grades_1.sort()
end_time = time.time()
time_diff = end_time - start_time

time_taken["Using list.sort"] = time_diff


msg = "Time Comparison: "
print(msg)
print('*' * len(msg))

for key in time_taken:
    msg = "{:<15} {}".format(key, time_taken[key])
    print(msg)


start_time = time.time()
custom_bs = sorted(grades, key=lambda x: x)

end_time = time.time()
time_diff = end_time - start_time

time_taken["Using sorted"] = time_diff


start_time = time.time()
grades.sort(key=lambda x: x)
end_time = time.time()
time_diff = end_time - start_time

time_taken["Using list.sort"] = time_diff


msg = "\n\nTime Comparison (With Key): "
print(msg)
print('*' * len(msg))

for key in time_taken:
    msg = "{:<15} {}".format(key, time_taken[key])
    print(msg)
