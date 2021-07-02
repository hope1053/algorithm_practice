N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key = lambda x:(x[-1], x[0]))
answer = 1
current_idx = 0
for idx in range(1, len(meetings)):
    if meetings[idx][0] >= meetings[current_idx][-1]:
        answer += 1
        current_idx = idx
print(answer)