def solution(participant, completion):
    NOT_COPMLE = 1
    table = {}
    for p in participant:
        table[p] = table.get(p,0) + 1 #table에서 p라는 key의 value를 리턴해라. 없으면 '0'이라는 디폴트값을 리턴해라.

    for c in completion:
        table[c] -= 1

    return [k for k,v in table.items() if v == 1] [0]