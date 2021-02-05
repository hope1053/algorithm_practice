def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    list1 = sorted(strings)
    answer = list()
    for i in range(len(strings)):
        answer.append(list1[i][1:])

    return answer