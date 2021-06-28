N = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)

prime_num = [True] * (max_num + 1)
prime_num[0], prime_num[1] = False, False

for num in range(2, max_num + 1):
    if prime_num[num]:
        for check_num in range(num * 2, max_num + 1, num):
            prime_num[check_num] = False

prime_num_list = set([idx for idx, value in enumerate(prime_num) if value])

count = 0
for num in num_list:
    if num in prime_num_list:
        count += 1

print(count)