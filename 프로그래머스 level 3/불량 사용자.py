import re
from collections import deque
from itertools import product

def solution(user_id, banned_id):
    banned_arr = list()
    for bann_condition in banned_id:
        get_id(bann_condition, banned_arr, user_id, banned_id)
    
    banned_arr = [sorted(tmp_arr) for tmp_arr in banned_arr]
    tmp_list = list(product(*banned_arr))
    answer_set = set()
    for answer_combi in tmp_list:
        if len(set(answer_combi)) == len(banned_id):
            answer_set.add(tuple(sorted(list(answer_combi))))
            
    return len(answer_set)
    
        
def get_id(bann_condition, banned_arr, user_id, banned_id):
    banned_arr.append([user for user in user_id if len(user) == len(bann_condition) and check_pos(user, bann_condition)])
                                   
def check_pos(user, bann_condition):
    check_condition = re.compile("(\W)").split(bann_condition)
    user = deque(user)
    
    for condition in check_condition:
        if condition == '':
            continue
        if condition == '*':
            user.popleft()
        else:
            tmp_string = ''
            for _ in range(len(condition)):
                tmp_string += user.popleft()
            if condition != tmp_string:
                return False
            
    return len(user) == 0