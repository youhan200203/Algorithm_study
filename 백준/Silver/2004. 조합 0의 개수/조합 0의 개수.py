n, m = map(int, input().split())

def count2(a):
    tmp = 0
    for i in range(1, 40):
        if 2 ** i <= a:
            tmp += a//(2**i)
    return tmp

def count5(a):
    tmp = 0
    for i in range(1, 20):
        if 5 ** i <= a:
            tmp += a//(5**i)
    return tmp

five = count5(n) - count5(m) - count5(n-m)
two = count2(n) - count2(m) - count2(n-m)
print(min(five, two))