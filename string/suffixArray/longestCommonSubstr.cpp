#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>
using namespace std;

ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        out << i << ' ';
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

    string s,t;
    cin >> s >> t;
    int n = s.size() + 1 + t.size();
    int sn = s.size();
    int tn = t.size();
    sa.resize(n);
    pos.resize(n);
    lcp.resize(n);

    make_suffix_array(s+"$"+t);
    make_lcp_array(s+"$"+t);

    auto check_diff_substr = [&] (int a, int b) -> bool{
        if (a>b) swap(a,b);
        return (a < sn) && (sn+1 <= b) && (b < n);
    };

    int ans = 0;
    int ans_idx = 0;
    for (int i=1; i<n; i++){
        if (check_diff_substr(sa[i-1], sa[i]) == false)
            continue;
        
        if (lcp[i] > ans){
            ans = lcp[i];
            ans_idx = sa[i];
        }
    }

    cout << ans << endl;
    cout << (s+"$"+t).substr(ans_idx,ans);
    return 0;
}