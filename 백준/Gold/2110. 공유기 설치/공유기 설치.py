import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for i in range(n):
    houses.append(int(input()))

houses.sort()
left = 1
right = houses[-1] - houses[0]
result = 0 
while left <= right:
    mid = (left+right)//2
    start = houses[0]
    count = 1
    while True:
        for house in houses:
            if house - start >= mid: #
                count += 1
                start= house
                if count >= c:
                    left = mid+1
                    result = mid
                    break
            # s += dist[i]
            # if s >= mid: 거리 누적합...이 아니라 그냥 현재 집과의 위치를 빼면 되는 거였음ㅠ
            #     start = i+1
            #     s = 0
            #     count += 1
        else: 
            right = mid-1
        break
print(result)
