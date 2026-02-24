from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*(m+1) for _ in range(n+1)] 
    queue = deque([(1, 1)])
    visited[1][1] = 1
    count = 0
    while queue:
        a, b = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_a, next_b = a+dx, b+dy
            if 1 <= next_a <= n and 1 <= next_b <= m:
                if next_a == n and next_b == m:
                    return visited[a][b] + 1
                if visited[next_a][next_b] == False and maps[next_a-1][next_b-1] == 1:
                    visited[next_a][next_b] = visited[a][b] + 1
                    queue.append((next_a, next_b))
    return -1