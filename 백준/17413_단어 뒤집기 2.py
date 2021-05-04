S = input()
inBracket = False
tmp_word = str()
answer = str()

for word in S:
    if word == ' ':
        if not inBracket:
            answer += tmp_word[::-1] + " "
            tmp_word = ""
        else:
            answer += " "
    elif word == '<':
        answer += tmp_word[::-1] + '<'
        inBracket = True
        tmp_word = str()
    elif word == '>':
        answer += '>'
        inBracket = False
    else:
        if inBracket:
            answer += word
        else:
            tmp_word += word

if tmp_word:
    answer += tmp_word[::-1]

print(answer)

# 사람이 이렇게 멍청해질 수 있구나...를 알게 해준 문제...^^...