from datetime import datetime
def change(string):
    string = string.replace('C#', 'c')
    string = string.replace('D#', 'd')
    string = string.replace('F#', 'f')
    string = string.replace('G#', 'g')
    string = string.replace('A#', 'a')
    return string


def get_time(str1, str2):
    dateFormatter = "%H:%M"
    str1 = datetime.strptime(str1, dateFormatter)
    str2 = datetime.strptime(str2, dateFormatter)
    return int((str2-str1).seconds / 60)
    
def solution(m, musicinfos):
    # 내가 찾는 음표 리스트로 만들기
    m = change(m)
    # 딕셔너리 만들기
    music_table = list() # 각 곡별로 곡 제목 : 플레이 된 악보 넣을 dictionary
    for idx, value in enumerate(musicinfos):
        temp = value.split(',') # 각 정보를 separate함
        # duration을 계산해서 해당 곡의 총 악보를 딕셔너리에 넣어줌)
        duration = get_time(temp[0], temp[1])
        note = change(temp[3])
        a,b = divmod(duration, len(note))
        note_arr = note * (a) + note[:b]
        if m in note_arr:
            music_table.append([idx, duration, temp[2]])
    if len(music_table) > 0:
        music_table.sort(key = lambda x:(-x[1], x[0]))
        return music_table[0][2]

    return '(None)'