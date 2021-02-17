def solution(N, stages):
    temp = []
    for i in range(1, N+1):
        if len([item for item in stages if item >= i]) == 0:
            temp.append([i, 0])
        else:
            failure = stages.count(i) / len([item for item in stages if item >= i])
            temp.append([i, failure])
    answer = sorted(temp, key = lambda x:x[1], reverse = True)
    return [i[0] for i in answer]