def biggerIsGreater(word):
    word = list(word)
    
    def get_bigger_idx(second):
        for idx in range(len(word) - 1, second - 1, -1):
            if word[idx] > word[second]:
                return idx
    
    first, second = len(word) - 1, len(word) - 2
    
    while second >= 0 and word[second] >= word[first]:
        first -= 1
        second -= 1
        
    if second == -1:
        return "no answer"
        
    bigger_idx = get_bigger_idx(second)
    word[second], word[bigger_idx] = word[bigger_idx], word[second]
    answer = word[:second + 1] + list(reversed(word[second + 1:]))
    
    return ''.join(answer)