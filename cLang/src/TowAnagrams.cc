#include <iostream>
#include <algorithm>
using namespace std;

// 辞書順の大きさを比較
// A < Bを求める
int main() {
    string s, t;
    cin >> s >> t;

    string beforeSort = s;
    string afterSort = t;
    sort(beforeSort.begin(), beforeSort.end());
    sort(afterSort.begin(), afterSort.end(), greater<int>());

    string ans = "No";
    if(beforeSort < afterSort) {
        ans = "Yes";
    }
    cout << ans << endl;
}