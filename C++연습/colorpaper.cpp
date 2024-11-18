#include <iostream>
#include <vector>
using namespace std;

void patch(int x, int y, int w, int h, int n, vector<vector<int>> *grid);
const int GRID_SIZE = 1001;

int main(){
    int n;
    cin >> n;
    vector<vector<int>> grid;
    grid.resize(GRID_SIZE,vector<int>(GRID_SIZE,-1));

    for (int i=0; i<n; i++){
        int x,y,w,h;
        cin >> x >> y >> w >> h;
        patch(x,y,w,h,i,&grid);
    }

    vector<int> ans(n,0);
    for (int i=0; i<GRID_SIZE; i++){
        for (int j=0; j < GRID_SIZE; j++){
            int col = grid[i][j];
            if (col != -1)
                ans[col] += 1;
        }
    }

    for (int i=0; i<n; i++){
        cout << ans[i] << endl;
    }

    return 0;
}

void patch(int x, int y, int w, int h, int n, vector<vector<int>> *grid){
    for (int i=y; i < y+h; i++){
        for (int j=x; j<x+w; j++){
            (*grid)[i][j] = n;
        }
    }
}