def solution(n, current_idx, cmd):
    COMMAND, NUM = 0, 1
    
    answer = ['O' for _ in range(n)]
    
    link_dict = {}
    deleted_list = []
    
    for idx in range(n):
        if idx == 0:
            link_dict[idx] = [None, idx+1]
        elif idx == n - 1:
            link_dict[idx] = [idx-1, None]
        else:
            link_dict[idx] = [idx-1, idx+1]
            
    cmd = [command.split(" ") for command in cmd]
    
    for command in cmd:
        # 이동하는 경우(위, 아래)
        if command[COMMAND] == 'D':
            for _ in range(int(command[NUM])):
                current_idx = link_dict[current_idx][1]
        elif command[COMMAND] == 'U':
            for _ in range(int(command[NUM])):
                current_idx = link_dict[current_idx][0]
        # 삭제하는 경우(처음, 마지막, 중간 각각의 경우)
        elif command[COMMAND] == 'C':
            before, after = link_dict[current_idx]
            deleted_list.append((before, after, current_idx))
            if before == None:
                link_dict[after][0] = before
                current_idx = after
            elif after == None:
                link_dict[before][1] = after
                current_idx = before
            else:
                link_dict[before][1] = after
                link_dict[after][0] = before
                current_idx = after
        # 복구하는 경우(처음, 마지막, 중간 각각의 경우)
        elif command[COMMAND] == 'Z':
            before, after, deleted_idx = deleted_list.pop()
            
            if before == None:
                link_dict[after][0] = deleted_idx
            elif after == None:
                link_dict[before][1] = deleted_idx
            else:
                link_dict[before][1] = deleted_idx
                link_dict[after][0] = deleted_idx
                
            
    for data in deleted_list:
        idx = data[-1]
        answer[idx] = 'X'
        
    return ''.join(answer)