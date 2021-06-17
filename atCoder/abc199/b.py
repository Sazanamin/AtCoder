N = int(input())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

left = max(arrayA)
right = min(arrayB)

count = 0
length = (right - left) + 1
for i in range(length):
    count += 1

print(count)