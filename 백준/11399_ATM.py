N = int(input())
waiting_time = sorted(list(map(int, input().split())))
total_time = 0
for i in range(N):
    total_time += sum(waiting_time[:i+1])
print(total_time)