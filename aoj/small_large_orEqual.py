# ２つの整数 a, b を読み込んで、a と b の大小関係を出力するプログラムを作成して下さい。
input = list(input().split())
a = int(input[0])
b = int(input[1])

if a == b:
    print("a == b")
elif a > b:
    print("a > b")
elif a < b:
    print("a < b")
