import sys
input = sys.stdin.readline

def dfs(start):
    start_node = start
    path = [] #리스트 생성도 O(n)
    while True:
        if visited[start] != 0:
            break
        path.append(start)
        visited[start] = start_node

        next_node = nums[start]
        if visited[next_node] == start_node:
            start = path.index(next_node)
            for j in path[start:]: #for j in range(1, n+1)는 O(n)
                full_visited[j] = True
            break
        start = next_node

t = int(input())
for i in range(t):
    n = int(input())
    nums = [-1] + list(map(int, input().split()))
    full_visited = [False] * (n+1)
    visited = [0] * (n+1)
    for student in range(1, n+1):
        if not visited[student]:
            dfs(student)
    print(n - sum(full_visited))