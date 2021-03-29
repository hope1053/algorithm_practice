from itertools import combinations
def solution(relation):
    col_len = len(relation[0])
    row_len = len(relation)
    
    # 전체 조합 구하기
    candidate = list()
    for i in range(1, col_len+1):
        candidate.extend(combinations(range(col_len), i))
    
    # 유일성 따지기
    unique = []
    for combi in candidate:
        tmp = [tuple(item[i] for i in combi) for item in relation]
        if len(set(tmp)) == row_len:
            unique.append(combi)
            
    # 최소성 따지기
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                
    return len(answer)