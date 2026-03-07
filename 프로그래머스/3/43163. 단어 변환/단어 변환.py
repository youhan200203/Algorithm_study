#변환 가능한 리스트를 각 단어별로 정리해야함, begin + words에 대해서, 근데 words -> begin으로 다시 변환하면 안됨
from collections import Counter, deque

#그 다음에 bfs
#target이 words 안에 없으면 변환 불가능
def solution(begin, target, words):
    if target not in words:
        return 0
    words_lst = [begin] + words
    graph = [[0]*len(words_lst) for _ in range(len(words_lst))]
    for i in range(len(words_lst)): #해당 단어에 대해서
        for j in range(1, len(words_lst)): #이 단어로 이동할 수 있는지
            diff = Counter(words_lst[i]) - Counter(words_lst[j])
            if len(diff) == 1 and list(diff.values())[0] == 1:
                graph[i][j] = 1
    visited = [0]*(len(words_lst))
    queue = deque([0])
    visited[0] = 1
    while queue:
        start = queue.popleft()
        for i in range(len(words_lst)):
            print(i, visited)
            if graph[start][i] == 1 and visited[i] == 0:
                if words_lst[i] == target:
                    return visited[start]
                queue.append(i)
                visited[i] = visited[start] + 1
    answer = 0
    return answer



