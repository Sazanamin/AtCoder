if __name__ == "__main__":
    sInput = input()

    oddList = []
    evenList = []

    for i in range(len(sInput)):
        if i % 2 == 0:
            oddList.append(sInput[i])
        else:
            evenList.append(sInput[i])
    
    # 奇数と偶数で分けた文字列をそれぞれ全て連結させる
    oddStr = "".join(oddList)
    evenStr = "".join(evenList)

    if len(sInput) == 1:
        if oddStr.islower():
            print("Yes")
        else:
            print("No")

    if oddStr.islower() and evenStr.isupper():
        print("Yes")
    else:
        print("No")
