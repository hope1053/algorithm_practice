def check_min(i, j):
    white_count = 0
    black_count = 0

    for y in range(i, i+8):
        for x in range(j, j+8):
            if (y - i) % 2 == 0:
                if (x - j) % 2 == 0:
                    if chess_board[y][x] == 'B':
                        white_count += 1
                    else:
                        black_count += 1
                elif (x - j) % 2 == 1:
                    if chess_board[y][x] == "W":
                        white_count += 1
                    else:
                        black_count += 1
            else:
                if (x - j) % 2 == 0:
                    if chess_board[y][x] == 'B':
                        black_count += 1
                    else:
                        white_count += 1
                elif (x - j) % 2 == 1:
                    if chess_board[y][x] == "W":
                        black_count += 1
                    else:
                        white_count += 1

    answer.append(min(white_count, black_count))

H, W = map(int, input().split())
chess_board = [list(input()) for _ in range(H)]
answer = list()

for i in range(H - 7):
    for j in range(W - 7):
        check_min(i, j)

print(min(answer))