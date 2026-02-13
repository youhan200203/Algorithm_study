import sys

for line in sys.stdin:
    l = u = n = s = 0
    lst = list(line)
    for i in lst:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            n += 1
        else:
            s += 1
    print(l, u, n, s-1)


