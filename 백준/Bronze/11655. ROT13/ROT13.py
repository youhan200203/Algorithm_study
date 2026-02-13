word = input()
result = ['*']*len(word)
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
 'y', 'z']
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
 'Y', 'Z']
for i in range(len(word)):
    if word[i].islower():
        idx = low.index(word[i])
        result[i] = low[(idx + 13)%26]
    elif word[i].isupper():
        idx = up.index(word[i])
        result[i] = up[(idx + 13)%26]
    else:
        result[i] = word[i]
print(''.join(result))