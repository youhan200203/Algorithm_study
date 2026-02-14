n = int(input())
result = []
if n == 0:
    print(0)
else:
    while n:
        r = n % (-2)
        n = n // (-2)
        if r == -1:
            r = 1
            n += 1
        result.append(r)
    result.reverse()
    print(''.join(map(str,result)))