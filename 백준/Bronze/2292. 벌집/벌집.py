n = int(input())

sequence= [1]
idx = 1
while sequence[-1] < n:
    sequence.append(sequence[-1]+6*idx)
    idx += 1
print(len(sequence))