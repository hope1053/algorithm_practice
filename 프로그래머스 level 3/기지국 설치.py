import math

def solution(n, stations, w):
    answer = 0
    not_installed_dis = list()
    
    for index in range(1, len(stations)):
        not_installed_dis.append(stations[index] - stations[index-1] - 1 - 2 * w)
    not_installed_dis.extend([stations[0] - w - 1, n - stations[-1] - w])

    elec_range = 2 * w + 1
    
    for dis in not_installed_dis:
        answer += math.ceil(dis / elec_range)
        
    return answer