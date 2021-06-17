import math
import itertools

S = list(input())

# 存在する数を配列に格納する
existNumbers = []
noExistNumbers = []
unrememberedNumbers = []

for i in range(len(S)):
    if S[i] == 'o':
        existNumbers.append(i)
    if S[i] == 'x':
        unrememberedNumbers.append(i)
    if S[i] == '?':
        existNumbers.append(i)

print(existNumbers)


# 0を含めた数字4桁のパスワードのパターンを全て確認する(0000-9999をすべて見る)

