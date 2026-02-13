import sys
input = sys.stdin.readline

n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
d = [-1]*n 

for idx in range(n):
    if idx == 0:
        d[idx] = wine[0]
    elif idx == 1:
        d[idx] = wine[0] + wine[1]
    elif idx == 2:
        d[idx] = max(wine[0]+wine[1], wine[0]+wine[2], wine[1]+wine[2])
    else:
        d[idx] = max(d[idx-1], d[idx-2]+wine[idx], d[idx-3]+wine[idx-1]+wine[idx])
    idx+=1

print(d[n-1])

#많이 헤맸다. 우선 어차피 모든 d[i]를 계산해야 한다면, top-down 함수를 쓸 이유가 없고 bottom-up으로 올라가야 recursion error가 뜨지 않는다.
#또한 바로 전 열에서 +하고 그러는 게 아니라 그냥 깔끔하게 상태 개수만큼 뺀 열에서 경우의 수를 나누자