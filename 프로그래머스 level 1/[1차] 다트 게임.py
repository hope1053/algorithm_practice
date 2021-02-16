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