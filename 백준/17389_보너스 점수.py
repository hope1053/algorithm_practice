N, S = input(), input()

score, bonus = 0, 0

for idx in range(int(N)):
    if S[idx] == 'O':
        score += idx+1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)