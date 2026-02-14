import sys
input = sys.stdin.readline

n, b = map(int, input().split())
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
 'Y', 'Z']

new_lst = lst[:b]
result = []
while n >= b:
    result.append(new_lst[n%b])
    n = n//b
result.append(new_lst[n])
result.reverse()
print(''.join(result))