d={1:[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

def dp(idx):
    if idx in d:
        return d[idx]
    lst = [-1]*10
    for i in range(10):
        lst[i] = sum(dp(idx-1)[:i+1])
    d[idx]=lst
    return d[idx]
    
    

n=int(input())
for i in range(1, n+1):
    d[i] = dp(i)
print(sum(d[n])%10007)