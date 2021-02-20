# たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。
# input: a と b が１つの空白で区切られて与えられます。
# output: 面積と周の長さを１つの空白で区切って１行に出力して下さい。
input = list(input().split())
a = int(input[0])
b = int(input[1])
area = a * b
areaLength = (a*2) + (b*2)
print(str(area) + " " + str(areaLength))