# 1st_try
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

# 2nd_try
def second_solution(N, stages):
    NOT_CLEARED, REACHED = 0, 1
    stages = [stage - 1 for stage in stages]
    stage_cleared = [[0,0] for _ in range(N + 1)]
    
    for stage in stages:
        for i in range(stage + 1):
            stage_cleared[i][REACHED] += 1
            if i == stage:
                stage_cleared[i][NOT_CLEARED] += 1
                
    stage_cleared = [[value[NOT_CLEARED] / value[REACHED] if value[REACHED] != 0 else 0, idx + 1] for idx, value in enumerate(stage_cleared)][:N]
    stage_cleared.sort(key = lambda x:(-x[0], x[1]))
    
    return [idx for value, idx in stage_cleared]