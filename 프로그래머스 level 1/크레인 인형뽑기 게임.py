# 1st try
def solution(board, moves):
    stack = []
    count = 0
    for i in moves:
        for arr in board:
            if arr[i-1] != 0:
                stack.append(arr[i-1])
                arr[i-1] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack = stack[:-2]
                    count += 2
                break
    return count

# 2nd try
def solution(board, moves):
    stack = list()
    count = 0
    for move in moves:
        for idx, value in enumerate(board):
            if value[move-1] == 0:
                continue
            else:
                if len(stack) > 0 and stack[-1] == value[move-1]:
                    stack.pop()
                    count += 2
                else:
                    stack.append(value[move-1])
                board[idx][move-1] = 0
                break
    return count