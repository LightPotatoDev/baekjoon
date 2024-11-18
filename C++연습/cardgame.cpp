#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

int main(){
    vector<int> array_a;
    vector<int> array_b;

    int n;
    for (int i=0; i<10; i++){
        cin >> n;
        array_a.push_back(n);
    }
    for (int i=0; i<10; i++){
        cin >> n;
        array_b.push_back(n);
    }
    int score_a = 0;
    int score_b = 0;

    for (int i=0; i<10; i++){
        if (array_a[i] > array_b[i]){
            score_a += 3;
        }
        else if (array_a[i] < array_b[i]){
            score_b += 3;
        }
        else{
            score_a += 1;
            score_b += 1;
        }
    }
    cout << score_a << ' ' << score_b << endl;

    if (score_a > score_b){
        cout << "A";
    }
    else if (score_a < score_b){
        cout << "B";
    }
    else{
        char winner = 'D';
        for (int i=9; i >= 0; i--){
            if (array_a[i] > array_b[i]){
                winner = 'A';
                break;
            }
            else if (array_a[i] < array_b[i]){
                winner = 'B';
                break;
            }
        }
        cout << winner;
    }
    return 0;
}