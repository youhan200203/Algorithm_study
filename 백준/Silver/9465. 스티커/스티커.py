n = int(input())
for i in range(n):
    ncol = int(input())
    nums = [-1]*2
    top = list(map(int, input().split()))
    bottom = list(map(int, input().split()))
    
    dp = [0, 0, 0]

    for col in range(ncol):
        new_top = max(dp[1], dp[2]) + top[col]
        new_bottom = max(dp[0], dp[2]) + bottom[col]
        new_none = max(dp[0], dp[1])
        dp = [new_top, new_bottom, new_none]
    
    print(max(dp))

'''
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

가 기존 코드였으나 시간이 오래 걸렸다.
해당 문제가 dp 문제인 것을 알아챌 수 있는 신호는 '현재 열에서의 선택이 이전 열에서 무엇을 골랐는지에 영향을 받는다'는 것.
그리고 나는 위 선택, 아래 선택, 선택X의 3개의 상태가 아니라 
반대 선택, 선택X 그 다음 열에서 위, 선택X 그 다음 열에서 아래, 라는 괴상한 상태로 나누어 계산했더니 망한 듯.
'이전 열에서 무엇을 골랐는지'가 아니라 '다음 열에서 무엇을 할 수 있는지' 미래 값을 참조하려고 했기에 불완전
'''