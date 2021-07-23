N = int(input())
value_list = list(map(int, input().split()))
value_set_list = sorted(list(set(value_list)), reverse= True)
value_dict = dict()
for idx, value in enumerate(value_set_list):
    value_dict[value] = idx + 1
total_length = len(value_set_list)
answer = list()

for value in value_list:
    answer.append(total_length - value_dict[value])

for value in answer:
    print(value, end=' ')