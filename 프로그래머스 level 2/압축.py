def solution(msg):
    table = {chr(ord('A')+v-1):v for v in range(1,27) }
    answer = list()
    msg = list(msg)
    while len(msg) != 0:
        temp_str = msg[0]
        while temp_str in table.keys():
            msg.pop(0)
            if len(msg) == 0:
                break
            temp_str += msg[0]
        if temp_str not in table.keys():
            table[temp_str] = max(table.values()) + 1
            temp_str = temp_str[:-1]
        answer.append(table[temp_str])
    return answer