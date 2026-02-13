import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 10001
for i in range(n):
    lst[int(input())] += 1
for index, count in enumerate(lst):
    for i in range(count):
        print(index)