#include <iostream>
using namespace std;

int make_tri(int n);

int main(){
    
    int n;
    cin >> n;
    cout << make_tri(n);
    
    system("pause");
    return 0;
}

int make_tri(int n){
    int cnt = 0;
    for (int a=1; a<=n/3+1; a++){
        for (int b=a; b<=n; b++){
            int c = n-a-b;
            if (a<=b && b<=c && a+b > c){
                cnt += 1;
            }
        }
    }
    return cnt;
}