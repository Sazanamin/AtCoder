#include <iostream>
using namespace std;

int main() {
    int A, B, C, X;
    cin >> A >> B >> C >> X;

    int counter = 0;
    // 0の値が渡された時でもループできるように条件を~以下にしている
    for(int i = 0; i <= A; i++) {
        for(int j = 0; j <= B; j++) {
            for(int k = 0; k <= C; k++) {
                int total = (500*i) + (100*j) + (50*k);
                if(total == X) {
                    counter++;
                }
            }
        }
    }

    cout << counter << endl;
}