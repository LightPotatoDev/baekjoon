#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int dir = 0;
    int rev = 1;

    for (int i=0; i<n; i++){
        int a,b,d;
        cin >> a >> b >> d;
        rev = rev / a * b;
        if (d == 1){
            dir = 1-dir;
        }
    }

    cout << dir << ' ' << rev;
    return 0;
}