import re
def solution(str1, str2):
    jakard_1, jakard_2 = list(), list()
    inter, union = list(), list()

    idx = 0
    for _ in range(len(str1)-1):
        if re.search('[^a-zA-Z]', str1[idx] + str1[idx+1]):
            pass
        else:
            jakard_1.append((str1[idx] + str1[idx+1]).lower())
        idx += 1
    idx = 0
    for _ in range(len(str2)-1):
        if re.search('[^a-zA-Z]', str2[idx] + str2[idx+1]):
            pass
        else:
            jakard_2.append((str2[idx] + str2[idx+1]).lower())
        idx += 1

    if len(jakard_1) == 0 and len(jakard_2) == 0:
        return 65536

    temp = set([x for x in jakard_1 if x in jakard_2])
    print(temp)
    inter = list()
    for i in temp:
        print(i)
        for j in range(min(jakard_1.count(i), jakard_2.count(i))):
            inter.append(i)
    for i in inter:
        jakard_1.remove(i)
        jakard_2.remove(i)
    union = inter + jakard_1 + jakard_2
    
    similarity = (float(len(inter)) / float(len(union))) * 65536
    return int(similarity)