import sys
input = sys.stdin.readline

n, b = input().split()
b = int(b)
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
 'Y', 'Z']

new_lst = lst[:b]
sum = 0
for i in range(len(n)):
    sum += b**(len(n)-i-1)*new_lst.index(n[i])
print(sum)