word = input()
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dct = {}
for i in lst:
    dct[i] = -1

for i in range(len(word)):
    if dct[word[i]] != -1:
        continue
    dct[word[i]] = i
print(' '.join(str(i) for i in dct.values()))