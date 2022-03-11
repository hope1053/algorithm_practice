import math

def solution(n, k):
    # 1. n을 k진수로 변환
    # 2. 그 수를 string으로 변환 후 0으로 split한 list 생성
    # 3. 그 수들이 각가 소수인지 판단
    total_num = 0
    
    k_notation = trans_notation(n,k).split("0")
    
    for num in k_notation:
        if num != "" and is_prime_num(int(num)):
            total_num += 1
            
    return total_num
    
    
# n진법으로 변경하는 함수
def trans_notation(n, k) -> str:
    notation_num = ""
    quot, remainder = divmod(n, k)
    
    while quot > 0 or remainder > 0:
        notation_num = str(remainder) + notation_num
        quot, remainder = divmod(quot, k)
        
    return notation_num

# 소수 판단 함수
def is_prime_num(num):
    if num == 1:
        return False
    
    is_prime = True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
            
    return is_prime