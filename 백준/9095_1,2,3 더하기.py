# DP 풀이

n = int(input())
arr = [int(input()) for _ in range(n)]

case_arr = [0 for _ in range(11)]
case_arr[0], case_arr[1], case_arr[2], case_arr[3] = 0,1,2,4
for i in range(4, max(arr)+1):
    case_arr[i] = case_arr[i-1] + case_arr[i-2] + case_arr[i-3]

for num in arr:
    print(case_arr[num])