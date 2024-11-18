#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int calc_score(vector<int> vec){
    int res = 0;
    for (int i=0; i<=2; i++){
        for (int j=i+1; j<=3; j++){
            for (int k=j+1; k<=4; k++){
                int s = vec[i]+vec[j]+vec[k];
                res = max(res,s%10);
            }
        }
    }
    return res;
}

int main(){
    int n;
    cin >> n;

    int winner = 0;
    int winscore = 0;

    for (int i=0; i<n; i++){
        vector<int> cards(5,0);
        for (int j=0; j<5; j++){
            cin >> cards[j];
        }
        int score = calc_score(cards);
        if (score >= winscore){
            winscore = score;
            winner = i+1;
        }
    }

    cout << winner;
    return 0;
}