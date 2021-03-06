# 1st try
def solution(skill, skill_trees):
    answer = 0
    table = {}
    for idx, value in enumerate(skill):
        table[value] = idx
        
    for i in skill_trees:
        temp = []
        for j in i:
            if j in table:
                temp.append(table[j])
        search = True
        for idx, value in enumerate(temp):
            # 이전 순서의 스킬이 있는지 확인
            for i in range(value):
                if i not in temp:
                    search = False
                    break
            # 순서가 뒤섞였는지 확인
            if len(temp) > 1:
                if idx == len(temp) -1:
                    break
                if temp[idx] > temp[idx+1]:
                    search = False
                    break
        if search == True:
            answer += 1
        
    return answer

# 2nd try
from collections import deque
def solution(skill, skill_trees):
    count = 0
    for skills in skill_trees:
        skill_list = deque(skill)
        for item in skills:
            if item not in skill_list:
                continue
            if item == skill_list[0]:
                skill_list.popleft()
            else:
                break
        else:
            count += 1
            
    return count