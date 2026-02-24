def solution(numbers, target):
    count= 0
    stack=[(0, 0)]
    while stack:
        a, b = stack.pop()
        if a == len(numbers):
            if b == target:
                count += 1
                continue
            else:
                continue
        stack.append((a+1, b+numbers[a]))
        stack.append((a+1, b-numbers[a]))
    return count