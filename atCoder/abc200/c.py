N = int(input())
aArray = input().split()

count = 0
for item in aArray:
    left = int(aArray[i])
    right = int(aArray[i + 1])

    if left - right == 0:
        count = count + 1
    elif left - right % 200 == 0:
        count = count + 1
    