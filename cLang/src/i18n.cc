#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int sLength = s.size();
    int betweenNum = (sLength - 2);
    string ans = s[0] + to_string(betweenNum) + s[sLength - 1];
    cout << ans << endl;
}