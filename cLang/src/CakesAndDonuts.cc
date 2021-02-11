#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    string answer = "No";
    // 4ドルの倍数
    for(int i = 0; 4*i <= N; i++) {
        // 7ドルの倍数
        for(int j = 0; 7*j <= N - (4*i); j++) {
            // 4ドルと7ドルの倍数の合計値が N を超えていれば良いはず
            int total = (4*i) + (7*j);
            if(total >= N) {
                answer = "Yes";
            }
        }
    }
    
    cout << answer << endl;
}