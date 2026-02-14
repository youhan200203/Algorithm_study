import sys
from itertools import combinations

input = sys.stdin.readline

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    a = lst[0]
    nums = lst[1:]
    sum = 0
    for i, j in combinations(nums, 2):
        sum+=gcd(i, j)
    print(sum)


