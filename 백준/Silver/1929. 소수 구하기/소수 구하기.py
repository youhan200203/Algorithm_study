m, n = map(int, input().split())
count = 0
for num in range(m, n+1):
    if num == 1:
        continue
    f = int(num ** 0.5)
    for i in range(2, f+1):
        if num % i == 0:
            break
    else:
        print(num)