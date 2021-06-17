N = int(input())
mountainInfo = []
for i in range(N):
    mountainInfo.append(input().split())

heightSizes = []
for i in range(N):
    heightSizes.append(int(mountainInfo[i][1]))

heightSizes.sort(reverse=True)
secondSize = int(heightSizes[1])

for i in range(N):
    height = int(mountainInfo[i][1])
    if height == secondSize:
        print(mountainInfo[i][0])