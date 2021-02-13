def solution(phone_number):
    num_lst=list(phone_number)
    for i in range(len(num_lst)-4):
        num_lst[i]="*"

    return ''.join(num_lst)
