from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

def diff(arr):
    tmp = 0
    for i in range(1, len(arr)):
        tmp += abs(arr[i]-arr[i-1])
    return tmp

ma = 0
for permu in permutations(nums, n):
    x = diff(permu)
    if ma < x:
        ma = x
print(ma)