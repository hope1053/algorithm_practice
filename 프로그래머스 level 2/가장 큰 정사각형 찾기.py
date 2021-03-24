import itertools
def solution(board):
    W = len(board[0])
    H = len(board)
    for i in range(1, H):
        for j in range(1, W):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    return max(itertools.chain(*board)) ** 2