import time
import random

grades = []
time_taken = {}

print("\n\n\n\tList Type: Single Dimension")
print("\tList Size: 10000000")
print("\tData Type: Float")

for _ in range(10000000):
    grades.append(round(random.uniform(0.0, 10000000.0), 1))

using_sorted_without_key(grades)

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


msg = "\tTime Comparison: "
print("\n" + msg)

for key in time_taken:
    msg = "\t{:<15} {}".format(key, time_taken[key])
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


msg = "\n\n\tTime Comparison (With Key): "
print(msg)

for key in time_taken:
    msg = "\t{:<15} {}".format(key, time_taken[key])
    print(msg)

print("\n\n")
