n = int(input())
d=[-1]*(n+5)
d[1]=0
d[2]=1
d[3]=1
def dp(idx):
    if d[idx] != -1:
        return d[idx]
    d[idx] = 1 + min(dp(idx//3)+idx%3, dp(idx//2)+idx%2)
    return d[idx]

print(dp(n))