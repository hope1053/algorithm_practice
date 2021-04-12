def solution(genres, plays):
    p_list = list(zip(genres, plays))
    p_num, answer = list(), list()
    for g in set(genres):
        tmp = 0
        for p in p_list:
            if p[0] == g:
                tmp += p[1]
        p_num.append((g, tmp))
    p_num.sort(key = lambda x: x[1], reverse = True)
    
    for g in p_num:
        tmp = list()
        for idx, value in enumerate(p_list):
            if g[0] == value[0]:
                tmp.append((value[1], idx))
        answer.extend(sorted(tmp, key = lambda x: (-x[0],x[1]))[:2])
    
    return [x[1] for x in answer]