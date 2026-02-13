word = input()
lst = []
for i in range(len(word)):
    lst.append(word[i:])
lst.sort()
print('\n'.join(lst))