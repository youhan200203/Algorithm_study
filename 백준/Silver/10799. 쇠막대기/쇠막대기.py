n = input()
s = 0
sum = 0
for i in range(len(n)):
    if n[i] == '(':
        if n[i+1] == ')':
            sum += s-1
            s += 1
        else:
            s += 1
    else:
        sum += 1
        s -= 1

print(sum)