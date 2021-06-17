N = int(input().split()[0])

count = 0

for i in range(10**12):
    ansValue = (10 * i) + i
    for i in range(N):
        x = i + 1
        if ansValue == x:
            count += 1
    if i > N:
        break
print(count)
