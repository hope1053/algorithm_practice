def solution(record):
    answer = list()
    table = {}
    for data in record:
        if data.split()[0] == 'Enter' or data.split()[0] == 'Change':
            table[data.split()[1]] = data.split()[2]

    for data in record:
        if data.split()[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(table[data.split()[1]]))
        elif data.split()[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(table[data.split()[1]]))

    return answer
