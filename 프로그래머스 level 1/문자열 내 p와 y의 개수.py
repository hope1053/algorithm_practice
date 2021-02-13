def solution(s):
    cntp = 0
    cnty = 0
    for v in s:
        if v == "p" or v == "P":
            cntp += 1
        elif v == "y" or v == "Y":
            cnty += 1
    if cntp == cnty:
        return True
    else:
        return False