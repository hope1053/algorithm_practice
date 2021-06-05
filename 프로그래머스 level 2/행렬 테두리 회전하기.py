# dictionary 사용
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

# table 회전
import heapq
def solution_2(rows, columns, queries):
    table = [[0] * (columns + 1) for _ in range(rows + 1)]
    answer = list()
    # 테이블 생성
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            table[i][j] = (i - 1) * columns + j 
    # 쿼리 갯수가 하나인 경우 처리
    if len(queries) == 1:
        return [table[queries[0][0]][queries[0][1]]]
    # 쿼리가 2개 이상인 경우 각 쿼리별로 처리
    for query in queries:
        get_min(table, query, answer)
        
    return answer

def get_min_2(table, query, answer):
    start_row, start_col, end_row, end_col = query
    tmp_value, min_value = table[start_row][start_col], table[start_row][start_col]
    print(tmp_value)
    
    # 서쪽
    for i in range(start_row, end_row):
        table[i][start_col] = table[i + 1][start_col]
        min_value = min(min_value, table[i][start_col])
        
    # 남쪽
    for i in range(start_col, end_col):
        table[end_row][i] = table[end_row][i + 1]
        min_value = min(min_value, table[end_row][i])
        
    # 동쪽
    for i in range(end_row, start_row, -1):
        table[i][end_col] = table[i-1][end_col]
        min_value = min(min_value, table[i][end_col])
        
    # 북쪽
    for i in range(end_col, start_col, -1):
        table[start_row][i] = table[start_row][i - 1]
        min_value = min(min_value, table[start_row][i])
        
    table[start_row][start_col + 1] = tmp_value
    answer.append(min_value)