n = int(input())
one, two = map(int, input().split())

family = [[0] for _ in range(n+1)]

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)
    
visited = [-1] + [0] * (n)

def dfs(start, visited, family, two):
    queue = [start]
    visited[start] = 1
    while queue:
        start = queue.pop()
        for next_node in family[start]:
            if visited[next_node] == False:
                visited[next_node] = visited[start] + 1
                queue.append(next_node)
                if next_node == two:
                    return

dfs(one, visited, family, two)
print(visited[two]-1)