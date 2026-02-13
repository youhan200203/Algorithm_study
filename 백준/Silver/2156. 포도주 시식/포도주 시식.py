n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
d = [-1]*n 

idx= 0
while idx < n:
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