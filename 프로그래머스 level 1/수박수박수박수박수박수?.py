def solution(n):
    watermellon_l = []
    for i in range(n):
        if i % 2 == 0:
            watermellon_l.insert(i, "수")
        else:
            watermellon_l.insert(i, "박")
    return ("".join(watermellon_l))
