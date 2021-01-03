# Problem Statement: https://www.hackerrank.com/challenges/nested-list/problem
# Given the names and grades for each student in a class of  students, store
# them in a nested list and print the name(s) of any student(s) having the
# second lowest grade.

if __name__ == '__main__':
    constaint = int(input())
    if constaint >= 2 and constaint <= 5:
        scores = []

        # marksheet = [[input(), float(input())] for _ in range(n)]

        for i in range(0, constaint):
            name = input()
            score = float(input())
            scores.append([name, score])

    second_highest = sorted(list(set([marks for name, marks in scores])))[1]
    print('\n'.join([a for a, b in sorted(scores) if b == second_highest]))


# if __name__ == '__main__':
#     constaint = int(input())
#     if constaint >= 2 and constaint <= 5:
#         scores = []
#         for i in range(0, constaint):
#             name = input()
#             score = float(input())
#             scores.append([name, score])

#         # scores = [['Harry', 37.21], ['Berry', 37.21], [
#         #     'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#         print(scores)
#         scores.sort(key=lambda x: x[1])
#         print(scores)
#         second_best = scores[1][1]
#         print(second_best)
#         find_sb = []
#         for score in scores:
#             if score[1] == second_best:
#                 find_sb.append(score)
#         print(find_sb)
#         find_sb.sort(key=lambda x: x[0])
#         for fsb in find_sb:
#             print(fsb[0])

# scores = [['Harry', 37.21], ['Berry', 37.21], [
#     'Tina', 37.2], ['Akriti', 36], ['Harsh', 39]]
# print(scores)
# scores.sort(key=lambda x: x[1])
# print(scores)
# second_best = scores[1][1]
# print(second_best)
# find_sb = []
# for score in scores:
#     if score[1] == second_best:
#         find_sb.append(score)
# print(find_sb)
# find_sb.sort(key=lambda x: x[0])
# for fsb in find_sb:
#     print(fsb[0])
