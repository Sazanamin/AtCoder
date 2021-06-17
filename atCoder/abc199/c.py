# 文字の長さ
N = int(input())
# 2Nの長さの文字列
targetStr = input()
# クエリの数
queryNumber = int(input())

# 入力したクエリを詰める
query = []
for i in range(queryNumber):
    inputQuery = list(map(int, input().split()))
    query.append(inputQuery)

for i in range(queryNumber):
    for j in range(query[i]):
        if query[i][0] == 1:
            # 入れ替え対象の文字を取得する
            firstChar = targetStr[query[i][1]]
            secondChar = targetStr[query[i][2]]
        
                




print(targetStr[0:N])
print(targetStr[N:])

