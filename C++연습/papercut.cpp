#include <iostream>
#include <vector>
using namespace std;

void cut_paper(int dir, int num, vector<int>&hori, vector<int>&verti){
    if (dir == 1){
        for (int i=num; i<hori.size(); i++){
            hori[i] += 1;
        }
    }
    if (dir == 0){
        for (int i=num; i<verti.size(); i++){
            verti[i] += 1;
        }
    }
}

int max_elements(vector<int>& vec){
    int seq = 1;
    int maxseq = 1;
    for (int i=1; i<vec.size(); i++){
        if (vec[i] == vec[i-1]){
            seq += 1;
        }
        else{
            seq = 1;
        }
        maxseq = max(seq,maxseq);
    }
    return maxseq;
}

ostream& operator << (ostream& s, vector<int> vec){
    for (int i=0; i<vec.size(); i++){
        s << vec[i] << " ";
    }
    return s;
}

int main(){
    int m,n;
    cin >> m >> n;
    vector<int> hori (m,0);
    vector<int> verti (n,0);

    int q;
    cin >> q;
    for (int i=0; i<q; i++){
        int dir,num;
        cin >> dir >> num;
        cut_paper(dir,num,hori,verti);
    }

    int max_h = max_elements(hori);
    int max_v = max_elements(verti);
    cout << max_h*max_v;

    return 0;
}