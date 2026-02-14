future, current = map(int, input().split())
digit = int(input())
nums = list(map(int, input().split()))
base = future ** (digit-1)
sum = 0
for i in range(digit):
    sum += nums[i] * base
    base = base // future
result = []
while sum:
    result.append(sum%current)
    sum = sum // current
result.reverse()
print(' '.join(map(str, result)))