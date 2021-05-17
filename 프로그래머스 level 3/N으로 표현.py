def solution(N, number):
    available_nums = [{0}, {N}]
    count = 1
    
    while True:
        if count > 8:
            return -1
        if number in available_nums[-1]:
            return count
        available_set = set()
        count += 1
        for i in range(1, count):
            for first_num in available_nums[i]:
                for second_num in available_nums[count - i]:
                    available_set.add(first_num + second_num)
                    available_set.add(first_num - second_num)
                    available_set.add(first_num * second_num)
                    if second_num != 0:
                        available_set.add(first_num // second_num)
        available_set.add(int(str(N)*count))
        available_nums.append(available_set)