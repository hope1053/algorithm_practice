def solution(s):
    t_arr, stack = list(), list()
    for i in s:
        temp, string = list(), str()
        if i == "}":
            while True:
                temp_str = stack.pop()
                if temp_str == "{":
                    if len(string) > 0:
                        temp.append(int(string))
                    break
                elif temp_str == ",":
                    if len(string) > 0:
                        temp.append(int(string))
                    string = ""
                else:
                    string = temp_str + string
        else:
            stack.append(i)
        if len(temp) > 0:
            t_arr.append(temp)

    t_arr.sort(key = lambda x:len(x))
    answer = t_arr[0]
    for i in range(1, len(t_arr)):
        answer.extend([x for x in t_arr[i] if x not in t_arr[i-1]])
    return answer