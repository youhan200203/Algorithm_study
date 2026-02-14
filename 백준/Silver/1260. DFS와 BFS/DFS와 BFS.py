import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
lst = [[] for _ in range(n+1)] 
#[[]] * (n+1)을 하면 안된다고 한다. 똑같은 리스트 참조하는 거라는데 솔직히 왜 저러는지 머리로는 이해 안감ㅠ 하지만 일단 확인

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(1, n+1):
    lst[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end= ' ')
    for next_node in lst[v]:
        if not visited[next_node]:
            dfs(next_node)

visited = [False] * (n+1)
dfs(v)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for next_node in lst[v]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
print()
visited= [False] * (n+1)
bfs(v)

#dfs, bfs 문제는 처음이라 챗지피티의 도움을 받아 이해해본다.
#dfs는 재귀로, bfs는 큐(덱)을 이용한다. 