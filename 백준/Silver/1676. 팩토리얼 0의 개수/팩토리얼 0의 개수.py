import sys
input = sys.stdin.readline

n = int(input())

def factorial(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp

result = 0
a = factorial(n)
while a % 10 == 0:
    result+=1
    a = a//10
print(result)
