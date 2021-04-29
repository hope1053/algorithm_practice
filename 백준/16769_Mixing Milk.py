capacity, milk = list(), list()

for idx in range(3):
    cap, am = map(int, input().split(' '))
    capacity.append(cap)
    milk.append(am)

for i in range(100):
    idx = i % 3
    next = (i+1) % 3
    if milk[idx] + milk[next] <= capacity[next]:
        milk[next] += milk[idx]
        milk[idx] = 0
    else:
        milk[idx] -= capacity[next] - milk[next]
        milk[next] = capacity[next]


for idx in range(3):
    print(milk[idx])