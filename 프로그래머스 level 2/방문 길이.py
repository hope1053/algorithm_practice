def solution(dirs):
    arr = list(dirs)
    tup, tmp = (0,0), tuple()
    table = {'U':(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
    loc, done_list = [(0,0)], list()
    dis = 0
    
    for direct in arr:
        a = tup[0] + table[direct][0]
        b = tup[1] + table[direct][1]
        tmp = (a,b)
        if tmp[0] < -5 or tmp[-0] > 5 or tmp[1] < -5 or tmp[1] > 5:
            continue
        tup = tmp
        loc.append(tup)
    
    for idx in range(1, len(loc)):
        if [loc[idx-1], loc[idx]] in done_list or [loc[idx], loc[idx-1]] in done_list:
            continue
        dis += abs(loc[idx-1][0] - loc[idx][0]) + abs(loc[idx-1][1] - loc[idx][1])
        done_list.append([loc[idx-1], loc[idx]])
        
    return dis