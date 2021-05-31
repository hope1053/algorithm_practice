def solution(routes):
    answer = 0
    CAR = len(routes)
    camera = -30001
    routes.sort(key = lambda x:x[1])
    
    for idx in range(CAR):
        if camera < routes[idx][0]:
            answer += 1
            camera = routes[idx][1]
            
    return answer