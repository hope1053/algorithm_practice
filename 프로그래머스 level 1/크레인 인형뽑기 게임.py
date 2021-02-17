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