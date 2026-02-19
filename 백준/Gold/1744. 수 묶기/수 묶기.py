import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))
nums.sort() #시간복잡도 O(NlogN)

boundary = 0
for i in range(n-1):
    a = nums[i]
    b = nums[i+1]
    if a <= 0 and b> 0:
        boundary = i+1 #boundary는 양수가 시작되는 경계
result = sum(nums)

start_idx = 0
end_idx = n-1 #아직 곱셈에 쓰이지 않은 끝 양수
while True:
    if len(nums) == 1:
        break
    if start_idx+1 < boundary: #음수와 0끼리는 곱하면 이득
        a= nums[start_idx]
        b= nums[start_idx+1]
        result += a*b-a-b 
        start_idx += 2
    elif end_idx-1 >= boundary:
        a= nums[end_idx]
        b= nums[end_idx-1]
        if a*b > a+b:
            result += a*b-a-b
        end_idx -= 2
    else:
        break
print(result)