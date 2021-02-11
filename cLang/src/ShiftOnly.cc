#include <iostream>
using namespace std;

int N;
int A[210];

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    int operationCounter = 0;

    // 操作が行える限り繰り返す
    while(true) {
        // A[i]が全て偶数かどうか判定するフラグ
        bool existOdd = false;
        for(int i = 0; i < N; i++) {
            if(A[i] % 2 != 0) {
                existOdd = true;
            }
        }

        // 奇数があったら操作を終了する
        if(existOdd) {
            break;
        }

        // 操作が行えるなら実際に操作を行う
        for(int i = 0; i < N; i++) {
            A[i] /= 2;
        }

        operationCounter++;
    }

    cout << operationCounter << endl;
}