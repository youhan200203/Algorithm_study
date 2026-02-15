import sys
input = sys.stdin.readline

n = int(input())
lst = [[0]]

def dfs(start: tuple, idx):
    stack = [start]
    count = 1
    visited[start[0]][start[1]] = idx
    while stack:
        start = stack.pop()
        start_x, start_y = start[0], start[1]
        next_nodes = [(start_x-1, start_y), (start_x+1, start_y), (start_x, start_y-1), (start_x, start_y+1)]
        for next_x, next_y in next_nodes:
            if next_x == 0 or next_x > n or next_y == 0 or next_y > n:
                continue
            if lst[next_x][next_y] == '0':
                continue
            if visited[next_x][next_y] == 0:
                stack.append((next_x, next_y))
                visited[next_x][next_y] = idx
                count += 1
    return count

for i in range(n):
    lst.append('0'+str(input().strip()))

visited = [[0]*(n+1) for _ in range(n+1)]
idx = 1
result = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if lst[i][j] == '1':
            if visited[i][j] == 0:
                count = dfs((i, j), idx)
                idx += 1
                result.append(count)

result.sort()

print(len(result))
print('\n'.join(map(str, result)))
