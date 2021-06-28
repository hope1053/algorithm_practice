M, N = map(int, input().split())

prime_num = [True] * (N + 1)
prime_num[0], prime_num[1] = False, False

for num in range(2, N + 1):
    if prime_num[num]:
        for change_num in range(num * 2, N + 1, num):
            prime_num[change_num] = False

prime_num_list = [idx for idx, value in enumerate(prime_num) if value == True and idx >= M]

for num in prime_num_list:
    print(num)