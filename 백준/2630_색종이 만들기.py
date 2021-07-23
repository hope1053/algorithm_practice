N = int(input())
paper_list = list()
answer = [0] * 2
for _ in range(N):
    paper_list.append(list(input().split()))

def check(x, y, n):
    init_val = paper_list[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper_list[i][j] != init_val:
                h_n = n // 2
                check(x, y, h_n)
                check(x, y + h_n, h_n)
                check(x + h_n, y, h_n)
                check(x + h_n, y + h_n, h_n)
                return

    answer[int(init_val)] += 1

check(0, 0, N)

for num in answer:
    print(num)