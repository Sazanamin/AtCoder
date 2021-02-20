import math

N = int(input())


point = 0
for i in range(N):
    value = input().split()

    date = value[0]
    price = int(value[1])
    if '3' in date:
        point += math.floor((price * 0.03))
    elif '5' in date:
        point += math.floor((price * 0.05))
    else:
        point += math.floor((price * 0.01))

print(point)

