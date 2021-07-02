N, M = map(int, input().split())
poketmon_list = list()
poketmon_dict = dict()
for i in range(N):
    name = input()
    poketmon_list.append(name)
    poketmon_dict[name] = i + 1

for _ in range(M):
    quiz = input()
    if quiz.isdigit():
        print(poketmon_list[int(quiz)-1])
    else:
        print(poketmon_dict[quiz])