import sys
input = sys.stdin.readline

n = int(input())
queue = []
front = 0
rear = 0
for i in range(n):
    line = input().split()
    if line[0] == 'push':
        queue.append(line[1])
        rear += 1
    elif line[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(queue[front])            
    elif line[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(queue[-1])   
    elif line[0] == 'size':
        print(rear-front)
    elif line[0] == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    else:
        if front == rear:
            print(-1)
        else:
            print(queue[front])
            front+=1