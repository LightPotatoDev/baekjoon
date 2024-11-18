#include <iostream>
#include <vector>
using namespace std;

void make_relation(vector<int> v, vector<vector<int>> *rel);
void print_relation(vector<vector<int>> *rel);

int main(){
    int n;
    cin >> n;

    vector<vector<int>> table;
    table.resize(n,vector<int>(5,0));
    vector<vector<int>> relation;
    relation.resize(n,vector<int>(n,0));
    
    for (int i=0; i<n; i++){
        for (int j=0; j<5; j++){
            cin >> table[i][j];
        }
    }

    for (int j=0; j<5; j++){
        vector<vector<int>> grade(9);
        for (int i=0; i<n; i++){
            int g = table[i][j];
            grade[g-1].push_back(i);
        }
        for (int g=0; g<9; g++){
            if (grade[g].size() > 1){
                make_relation(grade[g], &relation);
            }
        }
    }

    int ans = 0;
    int knows = -1;

    for (int i=0; i<n; i++){
        int s = 0;
        for (int j=0; j<n; j++){
            s += relation[i][j];
        }
        if (s > knows){
            ans = i+1;
            knows = s;
        }
    }
    cout << ans;

    return 0;
}

void make_relation(vector<int> v, vector<vector<int>> *rel){
    for (int i=0; i < v.size(); i++){
        for (int j = 0; j < v.size(); j++){
            if (v[i] != v[j]){
                (*rel)[v[i]][v[j]] = 1;
            }
        }
    }
}

void print_relation(vector<vector<int>> *rel){
    cout << endl;
    for (int i=0; i < (*rel).size(); i++){
        for (int j = 0; j < (*rel).size(); j++){
            cout << (*rel)[i][j] << ' ';
        }
        cout << endl;
    } 
}