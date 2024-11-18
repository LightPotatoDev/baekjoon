#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int n = 0;
int sqrt_n = 0;
vector<int> a;
vector<int> ans;

struct Query{
    int idx;
    int left;
    int right;
    Query(int i, int l, int r): idx(i), left(l), right(r) {}
    bool operator < (const Query &q) const {
        if (left / sqrt_n != q.left / sqrt_n) return (left / sqrt_n < q.left / sqrt_n);
        return right < q.right;
    }
};

ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        out << i << ' ';
    }
    out << '\n';
    return out;
}

ostream& operator << (ostream& out, const vector<Query>& v){
    for (Query i : v){
        out << i.idx <<  ' ' << i.left << ' ' << i.right << " / ";
    }
    out << '\n';
    return out;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    sqrt_n = sqrt(n);
    a.resize(n);
    for (int i=0; i < n; i++){
        cin >> a[i];
    }
    
    int m;
    vector<Query> queries;
    cin >> m;
    ans.resize(m);

    for (int i=0; i<m; i++){
        int l,r;
        cin >> l >> r;
        queries.push_back(Query(i,l-1,r-1));
    }
    sort(queries.begin(), queries.end());

    int res = 0;
    int left = queries[0].left;
    int right = queries[0].right;
    vector<int> unique(1e6+1);
    for (int i=left; i<=right; i++){
        if (unique[a[i]] == 0) res += 1;
        unique[a[i]] += 1;
    }
    ans[queries[0].idx] = res;

    for (int i=1; i<m; i++){
        while(queries[i].left < left){
            left -= 1;
            if (unique[a[left]] == 0) res += 1;
            unique[a[left]] += 1;
        }
        while(queries[i].left > left){
            if (unique[a[left]] == 1) res -= 1;
            unique[a[left]] -= 1;
            left += 1;
        }
        while(queries[i].right < right){
            if (unique[a[right]] == 1) res -= 1;
            unique[a[right]] -= 1;
            right -= 1;
        }
        while(queries[i].right > right){
            right += 1;
            if (unique[a[right]] == 0) res += 1;
            unique[a[right]] += 1;
        }
        ans[queries[i].idx] = res;
    }

    for (int i=0; i < m; i++){
        cout << ans[i] << '\n';
    }

    return 0;
}