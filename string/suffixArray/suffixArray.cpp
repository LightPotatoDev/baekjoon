#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        if (i != -1)
            out << i << ' ';
        else
            out << 'x' << ' ';
    }
    out << '\n';
    return out;
}

vector<int> sa;  //suffix array
vector<int> pos; //group number
vector<int> lcp;
void make_suffix_array(string s){

    int n = s.size();
    int d = 1;

    for (int i=0; i<n; i++){
        sa[i] = i;
        pos[i] = s[i];
    }

    auto cmp = [&](int i, int j)->bool{
        if (pos[i] != pos[j])
            return pos[i] < pos[j];

        i += d;
        j += d;
        if (i < n && j < n)
            return pos[i] < pos[j];
        else
            return i > j;
    };

    for (d=1; ; d*=2){
        sort(sa.begin(), sa.end(), cmp);
        vector<int> tmp(n);
        
        for(int i=0; i<n-1; i++){
            tmp[i+1] = tmp[i] + cmp(sa[i], sa[i+1]);
        }
        for(int i=0; i<n; i++){
            pos[sa[i]] = tmp[i];
        }

        if (tmp[n-1] == n-1) break;
    }
}

void make_lcp_array(string s){
    int n = s.size();
    for (int i=0, k=0; i<n; i++, k=max(k-1,0)){
        if (pos[i] == 0)
            continue;

        for (int j=sa[pos[i]-1]; s[i+k] == s[j+k]; k++);
        
        lcp[pos[i]] = k;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;
    int n = s.size();
    sa.resize(n);
    pos.resize(n);
    lcp.resize(n);
    fill(lcp.begin(),lcp.end(),-1);

    make_suffix_array(s);
    make_lcp_array(s);

    for (int i=0; i<n; i++){
        cout << sa[i] << '\n';
    }
    
    return 0;
}