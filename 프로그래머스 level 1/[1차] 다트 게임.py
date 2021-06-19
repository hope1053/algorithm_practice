# 1st_try
import re

def solution(dartResult):
    answer = []
    SDT = {"S":1, "D":2, "T":3}
    result = re.findall('\d+[SDT][\*\#]?', dartResult)

    for idx, value in enumerate(result):
        score = int(re.findall('\d+', value)[0]) ** (SDT[re.findall('[SDT]', value)[0]])
        if value[-1] == "#":
            score = -score
        elif value[-1] == "*":
            if idx != 0:
                answer[idx-1] *= 2
            score *= 2
        answer.append(score)

    return(sum(answer))

# 2nd_try
# 한 자리수 초과의 숫자의 문자열을 정규식으로 처리할때는 \d + << 꼭 기억하기!
import re
def second_solution(dartResult):
    multiple = {'S': 1, 'D': 2, 'T': 3}
    
    result = re.compile('(\d+)').split(dartResult)
    result = list(filter(lambda x: x != '', result))

    score_arr = list()
    
    for i in range(1, len(result), 2):
        if len(result[i]) < 2:
            score_arr.append(int(result[i-1]) ** multiple[result[i]])
        else:
            if result[i][-1] == '#':
                score_arr.append(-int(result[i-1]) ** multiple[result[i][0]])
            else:
                if score_arr:
                    score_arr[-1] *= 2
                score_arr.append(int(result[i-1]) ** multiple[result[i][0]] * 2)
                
    return sum(score_arr)