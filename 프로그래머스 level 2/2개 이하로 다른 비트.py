def solution(numbers):
    answer = list()
    
    for number in numbers:
        if number % 2:
            get_min(number, answer)
        else:
            answer.append(number + 1)
    
    return answer
        
def get_min(number, answer):
    bin_num = bin(number)[2:]
    if '0' not in bin_num:
        min_num = '10' + bin_num[1:]
    else:
        re_bin_num = bin_num[::-1]
        zero_idx = re_bin_num.index('0')
        real_zero_idx = -(zero_idx + 1)
        if real_zero_idx <= -3:
            min_num = bin_num[:real_zero_idx] + '10' + bin_num[real_zero_idx + 2:]
        else:
            min_num = bin_num[:real_zero_idx] + '10'
    
    answer.append(int(min_num, 2))