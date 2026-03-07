def dfs(start, visited, n, computers):
    queue = [start]
    visited[start] = 1
    while queue:
        start = queue.pop()
        for i in range(n):
            if computers[start][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return visited

def solution(n, computers):
    count = 0
    visited = [0]*n
    for j in range(n):
        if visited[j] != 1:
            visited = dfs(j, visited, n, computers)
            count += 1
    return count