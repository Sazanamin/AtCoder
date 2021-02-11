// 1以上 N 以下の整数のうち、10進法で各桁の和がA以上B以下であるものについて、総和を求めてください。
#include <iostream>
using namespace std;

int findSumOfDigit(int num) {
    int sum = 0;

    // num が 0 になるまで回す    
    while(num > 0) {
        sum += num % 10;
        num /= 10;
    }

    return sum;
}

int main() {
    int N, A, B;
    cin >> N >> A >> B;

    int total = 0;
    for(int i = 1; i <= N; i++) {
        int sum = findSumOfDigit(i);
        if(sum >= A && sum <= B) {
            total += i;
        }
    }

    cout << total << endl;
}

