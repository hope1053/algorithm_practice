import re
def solution(files):
    temp = list()
    for idx, value in enumerate(files):
        tp_str = re.match('[^0-9]+', value).group()
        tp_val = value.replace(tp_str, '')
        tp_int = re.match('[0-9]+', tp_val).group()
        temp.append([tp_str.lower(), tp_int, value, idx])
    
    temp.sort(key = lambda x:(x[0], int(x[1])))
    
    return [x[2] for x in temp]