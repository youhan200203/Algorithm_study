import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

left = 1
right = max(nums)
result = 0
while left <= right:
    mid = (left+right)//2
    s = 0
    for i in range(n):
        if nums[i] > mid:
            s+= nums[i] - mid
            if s >= m:
                left = mid + 1
                result = mid
                break
    else:
        right = mid - 1
print(result)