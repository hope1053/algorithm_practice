n = int(input())

def recursive(n):
    cache = [0] * (n+1)
    cache[1] = 1

    for i in range(2,n+1):
        cache[i] = cache[i-2] + cache[i-1]

    print(cache[n])

recursive(n)

---

n = int(input())

a, b = 0, 1
while n > 0:
    a, b = b, a+b
    n -= 1

print(a)
