N = int(input())

count = 0
answer = ""
current_int = 666

while True:
    if str(current_int).count("666") >= 1:
        count += 1
    if count == N:
        break
    current_int += 1
print(current_int)