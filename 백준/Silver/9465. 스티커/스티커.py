n = int(input())
for i in range(n):
    ncol = int(input())
    nums = [-1]*2
    for j in range(2):
        nums[j] = list(map(int, input().split()))
    for col in range(ncol-2, -1, -1):
        for row in range(2):
            if col == ncol-2:
                nums[row][col] = nums[row-1][col+1] + nums[row][col]
                continue
            nums[row][col] = max(nums[row-1][col+1], nums[row][col+2], nums[row-1][col+2]) + nums[row][col]
    print(max(nums[0][0], nums[1][0]))