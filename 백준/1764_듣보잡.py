N, M = map(int, input().split())

not_seen = set()
not_heard = set()

for _ in range(N):
    not_seen.add(input())

for _ in range(M):
    not_heard.add(input())

not_seen_heard = sorted(list(not_seen & not_heard))

print(len(not_seen_heard))
for name in not_seen_heard:
    print(name)