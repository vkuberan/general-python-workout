import time
import random
from faker import Faker


def custom_bubble_sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


fake = Faker()

scores = []
time_taken = {}
for _ in range(20000):
    name = fake.name()
    score = round(random.uniform(0.0, 100.0), 1)
    scores.append([name, score])

i = 1
for s in scores:
    msg = "{:<3} {:<30} {:>5}".format(i, s[0], s[1])
    print(msg)
    i += 1

start_time = time.time()
custom_bs = custom_bubble_sort(scores)
end_time = time.time()
time_diff = end_time - start_time

time_taken["CBS"] = time_diff


start_time = time.time()
custom_bs = sorted(scores, key=lambda x: x[1])
end_time = time.time()
time_diff = end_time - start_time

time_taken["Sorted"] = time_diff


start_time = time.time()
scores.sort(key=lambda x: x[1])
end_time = time.time()
time_diff = end_time - start_time

time_taken["InBuildSorted"] = time_diff

print(time_taken)
