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
def second_solution(board, moves):
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

# 3rd_try
def third_solution(board, moves):
    picked_dolls = list()
    dolls_count = 0
    moves = [num - 1 for num in moves]
    
    for move in moves:
        for row in board:
            if row[move] != 0:
                picked_dolls.append(row[move])
                row[move] = 0
                break
        if len(picked_dolls) >= 2 and picked_dolls[-1] == picked_dolls[-2]:
            picked_dolls.pop()
            picked_dolls.pop()
            dolls_count += 2
            
    return dolls_count