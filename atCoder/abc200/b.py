inputValue = input().split()
N = int(inputValue[0])
K = int(inputValue[1])

for i in range(K):
    if N % 200 == 0:
        N = N // 200
    else:
        N = int(str(N) + '200')

print(N)

