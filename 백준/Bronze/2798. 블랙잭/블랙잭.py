n, m = map(int, input().split())
nums = list(map(int, input().split()))
best = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = nums[i]+nums[j]+nums[k]
            if s <= m and s > best:
                best = s
print(best)
