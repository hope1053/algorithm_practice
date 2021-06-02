import heapq
def solution(rows, columns, queries):
    table = [[0] * (columns + 1) for _ in range(rows + 1)]
    answer = list()

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            table[i][j] = (i - 1) * columns + j 
    
    if len(queries) == 1:
        return [table[queries[0][0]][queries[0][1]]]
    
    for query in queries:
        get_min(table, query, answer)
        
    return answer

def get_min(table, query, answer):
    rotated_dict = dict()
    start_row, start_col, end_row, end_col = query
    # 1. 첫 줄, 마지막 줄 더하기
    for num in range(start_col, end_col + 1):
        rotated_dict[(start_row, num)] = table[start_row][num]
        rotated_dict[(end_row, num)] = table[end_row][num]
    # 2. 가운데 숫자들 더하기
    for num in range(start_row + 1, end_row):
        rotated_dict[(num, start_col)] = table[num][start_col]
        rotated_dict[(num, end_col)] = table[num][end_col]
    # 진짜로 돌려서 table에 반영하기
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            # 첫번째 범위
            if i == start_row and start_col < j <= end_col:
                table[i][j] = rotated_dict[(i, j-1)]
            # 두번째 범위
            elif start_row < i <= end_row and j == end_col:
                table[i][j] = rotated_dict[(i-1, j)]
            # 세번째 범위
            elif i == end_row and start_col <= j < end_col:
                table[i][j] = rotated_dict[(i, j+1)]
            elif start_row <= i < end_row and j == start_col:
                table[i][j] = rotated_dict[(i+1, j)]
                
    answer.append(min(rotated_dict.values()))