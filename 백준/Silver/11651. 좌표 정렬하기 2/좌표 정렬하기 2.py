import sys
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

points.sort(key=lambda x: (x[1], x[0])) #각 원소에 대해 key 함수의 결과값 기준으로 정렬

print('\n'.join(f'{str(a)} {str(b)}' for a, b in points))

#삽입 정렬로 해봤는데 시간 초과ㅠ