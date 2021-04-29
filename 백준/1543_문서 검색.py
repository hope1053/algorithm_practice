word = input()
search = input()
count = 0
LEN = len(search)
i = 0
while i < len(word):
    if word[i:i + LEN] == search:
        count += 1
        i += LEN
    else:
        i += 1

print(count)