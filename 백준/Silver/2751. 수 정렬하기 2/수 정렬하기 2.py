import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
print('\n'.join(str(num) for num in nums))