n, m, k = map(int, input().split())
remain = n+m-k
print(min(n//2, m, remain//3))

'''
n, m, k = map(int, input().split())
max_nteam = min(n//2, m)
if max_nteam*3 + k > n+m:
    max_nteam -= ((max_nteam*3+k) - (n+m)) / 3
    print(int(max_nteam))
else:
    print(max_nteam)
'''