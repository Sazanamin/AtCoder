baseInput = input().split()

a = int(baseInput[0])
b = int(baseInput[1])
c = int(baseInput[2])

left = (a**2) + (b**2)

right = c**2

if left < right:
    print('Yes')
else:
    print('No')
