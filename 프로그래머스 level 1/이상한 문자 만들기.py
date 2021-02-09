def solution(s):
    words = []
    word_list = s.split(' ')
    for i in range(len(word_list)):
        answer = ""
        for j in range(len(word_list[i])):
            if j % 2 == 0:
                answer += word_list[i][j].upper()
            else:
                answer += word_list[i][j].lower()
        words.append(answer)
    return(' '.join(words))
