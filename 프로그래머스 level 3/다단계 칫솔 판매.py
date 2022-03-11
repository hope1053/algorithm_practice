import math

def solution(enroll, referral, seller, amount):
    amount = [num * 100 for num in amount]
    
    refer_dict = dict()
    income_dict = {name : 0 for name in enroll}
    
    for index in range(len(enroll)):
        refer_dict[enroll[index]] = referral[index]
        
    for index in range(len(seller)):
        seller_name, income_amount = seller[index], amount[index]
        
        while seller_name != '-':
            amount_to_send = math.floor(income_amount * 0.1)
            amount_left = income_amount - amount_to_send
            
            if amount_left == 0:
                break
            
            income_dict[seller_name] += amount_left
            
            seller_name = refer_dict[seller_name]
            income_amount = amount_to_send
        
    return [income_dict[name] for name in enroll]