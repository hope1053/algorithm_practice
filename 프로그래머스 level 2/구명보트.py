def solution(people, limit):
    people.sort()
    boat = 0
    f_count = 0
    b_count = len(people) - 1
    while b_count - f_count >= 0:
        if people[f_count] + people[b_count] > limit:
            b_count -= 1
        else:
            f_count += 1
            b_count -= 1
        boat += 1
    return boat