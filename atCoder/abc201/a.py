aList = list(map(int, input().split()))

aList.sort()

a1 = aList[0]
a2 = aList[1]
a3 = aList[2]

left = a2 - a1
right = a3 - a2

if left - right == 0:
    print('Yes')
else:
    print('No')
