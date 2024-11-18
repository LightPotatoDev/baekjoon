#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int SIZE = 5*1e5;

void update(vector<int>& tree, int pos, int set, int start = 0, int end = SIZE-1, int node = 1){
    if (!(start <= pos && pos <= end)) return;
    tree[node] = max(tree[node], set);
    if (start == end) return;
    int mid = (start+end)/2;
    update(tree, pos, set, start, mid, node*2);
    update(tree, pos, set, mid+1, end, node*2+1);
}

int get_max(vector<int>& tree, int left, int right, int _max = 0, int start = 0, int end = SIZE-1, int node = 1){
    if (left > end || right < start){
        return 0;
    }
        if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start+end)/2;
    _max = max(get_max(tree, left, right, _max, start, mid, node*2) , get_max(tree, left, right, _max, mid+1, end, node*2+1));
    return _max;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,k,d,ans;
    cin >> n >> k >> d;
    ans = 0;
    vector<int> a(n);
    vector<int> max_tree(SIZE*4);
    vector<int> max_mod(k);
    for (int i=0; i<n; i++){
        cin >> a[i];
    }

    for (int i=0; i<n; i++){
        int m = a[i] % k;
        int value = max(max_mod[m], get_max(max_tree, a[i]-d, a[i]+d));
        ans = max(ans, value+1);
        max_mod[m] = value+1;
        update(max_tree, a[i], value+1);
    }
    cout << ans;

    return 0;
}