n, k = map(int, input().split())
ppl = list(range(1, n+1))
ans = []
i = 0
idx = k-1
while ppl:
    if idx >= len(ppl):
        idx = idx%len(ppl)
    ans.append(ppl.pop(idx))
    idx += k-1
print('<'+', '.join(str(i) for i in ans)+'>')