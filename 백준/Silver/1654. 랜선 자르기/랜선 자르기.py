import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
left = 1
right = sum(arr)//n
result = 1
while left <= right:
    mid = (left+right)//2
    s = 0
    for i in range(k):
        s += arr[i]//mid
    if s >= n:
        result = mid
        left = mid +1
    else:
        right = mid -1
print(result)
    