import sys
input = sys.stdin.readline

server = []
n = int(input())
for i in range(n):
    line = input().split()
    if line[0] == 'push':
        server.append(int(line[1]))
    elif line[0] == 'pop':
        if len(server) == 0:
            print(-1)
        else:
            print(server.pop())
    elif line[0] == 'top':
        if len(server) == 0:
            print(-1)
        else:
            print(server[-1])
    elif line[0] == 'size':
        print(len(server))
    elif line[0] == 'empty':
        if len(server) == 0:
            print(1)
        else:
            print(0)
