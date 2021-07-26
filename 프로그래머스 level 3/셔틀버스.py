from collections import deque
def solution(n, t, m, timetable):
    current_time = 540
    time_list = list()
    for time_string in timetable:
        hour, minute = time_string.split(':')
        time_list.append(int(hour) * 60 + int(minute))
    time_list.sort()
    time_list = deque(time_list)
    while n > 1:
        n -= 1
        able_member = m
        while time_list and time_list[0] <= current_time and able_member > 0:
            able_member -= 1
            time_list.popleft()
        current_time += t
    able_member_list = list()
    while time_list and time_list[0] <= current_time:
        able_member_list.append(time_list.popleft())
    if len(able_member_list) < m:
        latest_time = current_time
    else:
        latest_time = able_member_list[m-1] - 1

    latest_hour = str(latest_time // 60) if latest_time // 60 >= 10 else "0" + str(latest_time // 60)
    latest_min = str(latest_time % 60) if latest_time % 60 >= 10 else "0" + str(latest_time % 60)
    return latest_hour + ":" + latest_min