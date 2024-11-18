#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main(){
    string s1;
    string s2;
    cin >> s1 >> s2;
    unsigned long long ans = 0;

    for (size_t i=0; i<s1.size(); i++){
        for (size_t j=0; j<s2.size(); j++){
            int n1 = s1[i]-'0';
            int n2 = s2[j]-'0';
            ans += n1*n2;
        }
    }

    cout << ans;
    return 0;
}