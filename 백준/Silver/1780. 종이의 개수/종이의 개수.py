import sys
input = sys.stdin.readline

n = int(input())

count = {-1: 0, 0:0, 1:0}
def solve(r, c, size): #arr뿐만 아니라 size도 함께 매개변수에 포함해야 함
    start= num[r][c]
    for i in range(size):
        for l in range(size):
            if num[r+i][c+l] != start:
                new_size = size//3 
                for j in range(3):
                    for k in range(3):
                        solve(r+j*new_size, c+k*new_size, new_size)
                return
    count[start] += 1
    return count

num = []
for i in range(n):
    num.append(list(map(int, input().split())))
solve(0, 0, n)

print('\n'.join(map(str, count.values())))
