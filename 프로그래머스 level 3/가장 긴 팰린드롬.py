def solution(s):
    answer = 1
    
    for i in range(len(s) - 1):
        for j in range(i, len(s)):
            if check_palindrome(s[i:j+1]):
                answer = max(answer, j-i+1)
                
    return answer
                
def check_palindrome(candidate):
    return candidate == candidate[::-1]