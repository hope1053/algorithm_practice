# 주어진 문자열을 초 단위로 바꿔주는 함수
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def get_str(time_int):
    answer_arr = list()
    a, b = divmod(time_int, 3600)
    if a < 10:
        answer_arr.append('0' + str(a))
    else:
        answer_arr.append(str(a))
    a, b = divmod(b, 60)
    if a < 10:
        answer_arr.append('0' + str(a))
    else:
        answer_arr.append(str(a))
    if b < 10:
        answer_arr.append('0' + str(b))
    else:
        answer_arr.append(str(b))
    return ':'.join(answer_arr)

def solution(play_time, adv_time, logs):
    play_time = get_sec(play_time)
    adv_time = get_sec(adv_time)
    total_time = [0] * (play_time + 1)
    
    for log in logs:
        log = log.split('-')
        start, end = get_sec(log[0]), get_sec(log[1])
        total_time[start] += 1
        total_time[end] -= 1
    
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i-1]

    for i in range(1, len(total_time)):
        total_time[i] += total_time[i-1]

    
    max_time = 0
    answer_time = 0
    for ending in range(adv_time - 1, play_time):
        if ending >= adv_time:
            if max_time < total_time[ending] - total_time[ending - adv_time]:
                max_time = total_time[ending] - total_time[ending - adv_time]
                answer_time = ending - adv_time + 1
        else:
            if max_time < total_time[ending]:
                max_time = max(max_time, total_time[ending])
                answer_time = ending - adv_time + 1
            
    return get_str(answer_time)