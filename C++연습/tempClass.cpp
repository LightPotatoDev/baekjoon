#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<vector<int>> table;
    table.resize(n,vector<int>(n,0));
    vector<vector<int>> relation;
    relation.resize(n,vector<int>(n,0));
    
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cin >> table[i][j];
        }
    }

    for (int j=0; j<n; j++){
        vector<vector<int>> grade(9);
        for (int i=0; i<n; i++){
            int g = table[i][j];
            grade[g-1].push_back(i);
        }
        for (int g=0; g<9; g++){
            if (grade[g].size() > 1){
                for (int i=0; i<grade[g].size(); i++){
                    int s = grade[g][i];
                    relation[s][j] = 1;
                }
            }
        }
    }

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cout << relation[i][j] << ' ';
        }
        cout << endl;
    }
    system("pause");
    return 0;
}