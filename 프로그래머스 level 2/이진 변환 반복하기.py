def solution(s):
    zero_count, bin_count = 0, 0
    while s != "1":
        string = str()
        for i in s:
            if i == '1':
                string += i
            else:
                zero_count += 1
        c = len(string)
        s = str(bin(c))[2:]
        bin_count += 1
    return [bin_count, zero_count]