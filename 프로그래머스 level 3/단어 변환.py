from collections import deque, Counter

def solution(begin, target, words):
    if target not in set(words):
        return 0
    
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        changing_word, count = queue.popleft()
        for word in words:
            if check_difference(changing_word, word):
                if word == target:
                    return count + 1
                queue.append((word, count + 1))
                
def check_difference(changing_word, word):
    changing_dict = Counter(list(changing_word))
    word_dict = Counter(list(word))
    
    if len(changing_dict - word_dict) == 1:
        return True
    return False