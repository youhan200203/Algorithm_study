import sys
input = sys.stdin.readline

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
new_a = gcd(a, b)
print('1'*new_a)