n = int(input())
m = int(input())
link = [[0] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

visited = [True] + [False] * (n)

def dfs(start, visited, link):
    visited[start] = True
    queue = [start]
    while queue:
        start = queue.pop()
        for next_node in link[start]:
            if visited[next_node] == False:
                queue.append(next_node)
                visited[next_node] = True

dfs(1, visited, link)
print(sum(visited)-2)