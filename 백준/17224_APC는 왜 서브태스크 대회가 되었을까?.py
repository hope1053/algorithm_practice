n, l, k = map(int, input().split(' '))
score = list()

for _ in range(n):
    sub1, sub2 = map(int, input().split(' '))
    if sub2 <= l:
        score.append(140)
    elif sub1 <= l:
        score.append(100)
score.sort(reverse = True)

print(sum(score[:k]))