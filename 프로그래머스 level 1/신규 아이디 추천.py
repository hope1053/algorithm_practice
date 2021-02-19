import re
def solution(new_id):
    #1번 소문자로
    new_id = new_id.lower()
    #2번 허용되지 않는 문자 
    new_id = ''.join((re.findall('[0-9a-z-_.]+',new_id)))
    #3번 마침표 2번이상 연속된 부분을 하나의 마침표로 치환
    new_id = re.sub('[.]{2,}','.',new_id)
    #4번 마침표가 처음이나 끝에 위치하면 제거
    new_id = re.sub('^[.]','',new_id)
    new_id = re.sub('[.]$','',new_id)
    #5단계 빈문자열이라면 a대입
    if len(new_id) == 0:
        new_id += "a"
    #6단계 16자 이상이면 15자까지만 살려두고 뒤에 다 지움. 지우고 마지막이 마침표면 그것도 지움
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('[.]$','',new_id)
    #7단계 2자 이하면 마지막 문자를 길이가 3이 될 때까지 반복해서 붙임
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[len(new_id)-1]
    return(new_id)
