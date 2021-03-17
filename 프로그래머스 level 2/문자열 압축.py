def solution(s):
    result, length = str(), list()
    if len(s) == 1: return 1
    for token_length in range(1, len(s)//2 + 1):
        temp = s[:token_length]
        count = 1
        for j in range(token_length, len(s), token_length):
            if temp == s[j:j+token_length]:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[j:j+token_length]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + temp
        length.append(len(result))
        result = ""

    return min(length)