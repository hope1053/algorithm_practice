from collections import defaultdict
import math

def solution(fees, records):
    
    fee_record_dict = defaultdict(list)
    
    fee_list = []
    
    for record in records:
        record_time, car_num, in_or_out = record.split()
        fee_record_dict[car_num].append(time_to_min(record_time))
    
    for key, value in fee_record_dict.items():
        total_fee = calculate_fee(value, fees)
        fee_list.append((key, total_fee))
        
    fee_list.sort(key = lambda x:x[0])
    
    return [item[1] for item in fee_list]
        
def time_to_min(string_time):
    hour, minute = string_time.split(":")
    total_minute = int(hour) * 60 + int(minute)
    
    return total_minute

def calculate_fee(time_list, fees) -> int:
    BASIC_TIME, BASIC_FEE, OVER_TIME, OVER_FEE = fees
    LAST_TIME = time_to_min("23:59")
    
    total_fee = 0
    total_parking_time = 0
    
    if len(time_list) % 2 == 1:
        time_list.append(LAST_TIME)
        
    for time_index in range(len(time_list) // 2):
        in_time, out_time = time_list[time_index * 2], time_list[time_index * 2 + 1]
        
        total_parking_time += out_time - in_time
    
    if total_parking_time <= BASIC_TIME:
        total_fee += BASIC_FEE
    else:
        total_fee += BASIC_FEE + math.ceil((total_parking_time - BASIC_TIME) / OVER_TIME) * OVER_FEE

    return total_fee