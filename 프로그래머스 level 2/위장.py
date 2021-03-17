def solution(clothes):
    answer = 1 
    table = {}
    for i in clothes:
        if table.get(i[1], 'None') == 'None':
            table[i[1]] = [i[0]]
        else:
            table[i[1]].extend([i[0]])
    
    clothes = list(table.values())
    
    for i in clothes:
        answer *= (len(i)+1)
        
    return answer-1