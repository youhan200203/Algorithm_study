n = int(input())
d = {1:0, 2:1, 3:1}
def dp(idx):
    if idx in d:
        return d[idx]
    d[idx] = 1 + min(dp(idx//3)+idx%3, dp(idx//2)+idx%2)
    return d[idx]

print(dp(n))

#매번 -1을 해주기보다는, 나머지를 이용해 규칙을 만들어내 수학적으로 빠르게!