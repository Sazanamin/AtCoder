# ３つの整数a, b, cを読み込み、それらが a < b < cの条件を満たすならば"Yes"を、満たさないならば"No"を出力するプログラムを作成して下さい。
# Input: ３つの整数が空白で区切られて与えられます。
# Output: YesまたはNoを１行に出力して下さい。
if __name__ == "__main__":
    input = list(input().split())
    a = int(input[0])
    b = int(input[1])
    c = int(input[2])

    strResult = "Yes"
    if a >= c:
        strResult = "No"
    else: 
        if a >= b :
            strResult = "No"
        else:
            if(b >= c):
                strResult = "No"

    print(strResult)



