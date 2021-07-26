from collections import deque
def solution(n, t, m, timetable):
    current_time = 540
    # timetable 분으로 치환하고 정렬...?
    time_list = list()
    for time_string in timetable:
        hour, minute = time_string.split(':')
        time_list.append(int(hour) * 60 + int(minute))
    time_list.sort()
    time_list = deque(time_list)
    # n가 1보다 크면 m만큼 리스트에서 제거(단 해당 값이 버스가 온 시간보다 작거나 같아야함)
    while n > 1:
        n -= 1
        able_member = m
        while time_list and time_list[0] <= current_time and able_member > 0:
            able_member -= 1
            time_list.popleft()
    # 버스가 오는 간격만큼 추가해줌 시간에서
        current_time += t
    # n가 1이 된 경우, 마지막 버스이기 때문에 타야함 -> 현재 버스에 탈 수 있는 인원을 모두 모음
    able_member_list = list()
    while time_list and time_list[0] <= current_time:
        able_member_list.append(time_list.popleft())
    # 만약 해당 인원수가 버스에 탈 수 있는 인원수보다 적으면 버스가 오는 시간(current_time)에 가면 됨
    if len(able_member_list) < m:
        latest_time = current_time
    # 만약 해당 인원수가 버스에 탈 수 있는 인원수보다 크거나 같으면 마지막에 타는 ㄴ사람보다 -1분 빨리 가야함
    else:
        latest_time = able_member_list[m-1] - 1
    print(latest_time)
    latest_hour = str(latest_time // 60) if latest_time // 60 >= 10 else "0" + str(latest_time // 60)
    latest_min = str(latest_time % 60) if latest_time % 60 >= 10 else "0" + str(latest_time % 60)
    return latest_hour + ":" + latest_min