d= {1:1, 2:2}
def dp(idx):
    if idx in d:
        return d[idx]
    d[idx] = dp(idx-1) + dp(idx-2)
    return d[idx]

n = int(input())
print(dp(n)%10007)