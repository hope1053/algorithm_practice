N = int(input())
paper_list = list()
answer = [0] * 3

for _ in range(N):
    paper_list.append(list(map(int, input().split())))

def cut_paper(a, b, N):
    init_val = paper_list[a][b]
    for i in range(a, a+N):
        for j in range(b, b+N):
            if paper_list[i][j] != init_val:
                third_N = N // 3
                cut_paper(a, b, third_N)
                cut_paper(a, b + third_N, third_N)
                cut_paper(a, b + 2*third_N, third_N)

                cut_paper(a + third_N, b, third_N)
                cut_paper(a + third_N, b + third_N, third_N)
                cut_paper(a + third_N, b + 2*third_N, third_N)

                cut_paper(a + 2 * third_N, b, third_N)
                cut_paper(a + 2 * third_N, b + third_N, third_N)
                cut_paper(a + 2 * third_N, b + 2*third_N, third_N)
                return

    answer[init_val] += 1

cut_paper(0, 0, N)
answer = [answer[-1]] + answer[:-1]
for num in answer:
    print(num)