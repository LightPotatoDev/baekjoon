#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string>
using namespace std;

char decode(string s, string* msg);

int main(){
    int n;
    cin >> n;

    string message;
    cin >> message;

    string promise[8] = {
        "000000",
        "001111",
        "010011",
        "011100",
        "100110",
        "101001",
        "110101",
        "111010"
    };

    string ans;
    bool ok = true;

    for (int i=0; i<n; i++){
        string sub_msg = message.substr(i*6,i*6+6);
        char res = decode(sub_msg, promise);
        if (res == 0){
            cout << i+1;
            ok = false;
            break;
        }
        else{
            ans.push_back(res);
        }
    }

    if (ok){
        cout << ans;
    }
    return 0;
}

char decode(string s, string* promise){
    for (int i=0; i<8; i++){
        int error = 0;
        for (int j=0; j<6; j++){
            if (promise[i][j] != s[j]){
                error += 1;
            }
        }
        if (error <= 1){
            return 'A'+i;
        }
    }
    return 0;
}