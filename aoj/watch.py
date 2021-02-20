# 秒単位の時間 S が与えられるので、h:m:s の形式へ変換して出力してください。
# ここで、h は時間、m は 60 未満の分、s は 60 未満の秒とします。
input = int(input())
h = input / 3600
m = (input % 3600) / 60
s = (input % 3600) % 60
dispStr = "{}:{}:{}".format(int(h), int(m), int(s))
print(dispStr)