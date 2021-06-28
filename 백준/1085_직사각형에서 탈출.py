list_len = int(input())
word_list = list(set([input() for _ in range(list_len)]))

for word in sorted(word_list, key = lambda x:(len(x), x)):
    print(word)
