#include <iostream>
#include <string>
#include <vector>
using namespace std;

ostream& operator << (ostream& s, vector<int> vec){
    for (int i=0; i<vec.size(); i++){
        s << vec[i] << " ";
    }
    return s;
}

int main(){
    string s1;
    string s2;
    cin >> s1;
    cin >> s2;
    vector<int> s1_chars (26,0);
    vector<int> s2_chars (26,0);

    for (int i=0; i<s1.size(); i++){
        s1_chars[s1[i]-'a'] += 1;
    }
    for (int i=0; i<s2.size(); i++){
        s2_chars[s2[i]-'a'] += 1;
    }

    int ans = 0;
    for (int i=0; i<26; i++){
        ans += abs(s1_chars[i]-s2_chars[i]);
    }
    cout << ans;
    return 0;
}