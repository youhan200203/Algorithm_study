import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)] 
#[[]] * (n+1)을 하면 안된다고 한다. 똑같은 리스트 참조하는 거라는데 솔직히 왜 저러는지 머리로는 이해 안감ㅠ 하지만 일단 확인

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

ans_dfs = []

def dfs(v): #재귀 dfs를 쓰면 recursion error가 나서 스택 dfs를 배웠다
    stack = [v]
    visited[v] = True
    while stack:
        v = stack.pop()
        for next_node in lst[v]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

    
visited = [False] * (n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        count+=1
        dfs(i)
print(count)

# def bfs(v):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         v=queue.popleft()
#         ans_bfs.append(v)
#         for next_node in lst[v]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)