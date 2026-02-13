import sys
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
points.sort()
print('\n'.join(f'{a} {b}' for a, b in points))

#join은 리스트뿐만 아니라 for문의 iterable 객체도 받음