def solution(n):
    final_result = list()
    dfs(n, 0, [], final_result)
    return len(final_result)

def dfs(n, current_row, candidate, final_result):
    if current_row == n:
        final_result.append(candidate)
        return
    
    for col in range(n):
        if is_available(current_row, col, candidate):
            candidate.append(col)
            dfs(n, current_row + 1, candidate, final_result)
            candidate.pop()
    
def is_available(current_row, col, candidate):
    for idx, value in enumerate(candidate):
        if value == col or abs(current_row - idx) == abs(col - value):
            return False
    return True