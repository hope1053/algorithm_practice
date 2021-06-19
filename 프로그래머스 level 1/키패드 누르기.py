#1st_try
def solution(numbers, hand):
    left, right = 0, 0
    answer = ''
    place = [[0,3],[2,3]]
    case = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
        elif num in [3,6,9]:
            answer += 'R'
        else:
            left = sum(map(abs,([place[0][0] - case[num][0],place[0][1] - case[num][1]])))
            right = sum(map(abs,([place[1][0] - case[num][0],place[1][1] - case[num][1]])))
            if left == right:
                if hand == "left":
                    answer += 'L'
                else:
                    answer += 'R'
            elif left > right:
                answer += 'R'
            else:
                answer += 'L'
        if answer[-1] == 'L':
            place[0] = case[num]
        else:
            place[1] = case[num]


    return answer

#2nd_try
pos_dict = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2), 0: (3,1), '*': (3,0), '#': (3,2)}

def second_solution(numbers, hand):
    hand_letter = 'L' if hand == "left" else 'R'
    answer = ''
    current_left, current_right = '*', '#'
    left_set = {1, 4, 7}
    right_set = {3, 6, 9}
    
    for num in numbers:
        if num in left_set:
            answer += 'L'
            current_left = num
        elif num in right_set:
            answer += 'R'
            current_right = num
        else:
            answer += get_dis(current_left, current_right, num, hand_letter)
            if answer[-1] == 'L':
                current_left = num
            else:
                current_right = num
                
    return answer
            
def get_dis(current_left, current_right, num, hand_letter):
    move_to_pos = pos_dict[num]
    left_pos = pos_dict[current_left]
    right_pos = pos_dict[current_right]
    
    left_distance = abs(left_pos[0] - move_to_pos[0]) + abs(left_pos[1] - move_to_pos[1])
    right_distance = abs(right_pos[0] - move_to_pos[0]) + abs(right_pos[1] - move_to_pos[1])   
    
    if left_distance == right_distance:
        return hand_letter
    elif left_distance > right_distance:
        return 'R'
    else:
        return 'L'