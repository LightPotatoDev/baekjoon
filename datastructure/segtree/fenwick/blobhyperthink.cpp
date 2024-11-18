#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 1000000007;

void update(vector<long long>& tree, int start, int end, int node, int pos, long long add){
    if (!(start <= pos && pos <= end)) return;
    tree[node] = (tree[node] + add) % MOD;
    if (start == end) return;
    int mid = (start+end)/2;
    update(tree, start, mid, node*2, pos, add);
    update(tree, mid+1, end, node*2+1, pos, add);
}

long long get_sum(vector<long long>& tree, int start, int end, int node, int left, int right, long long sum){
    if (left > end || right < start){
        return 0;
    }
        if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start+end)/2;
    sum = (get_sum(tree, start, mid, node*2, left, right, sum) % MOD + get_sum(tree, mid+1, end, node*2+1, left, right, sum) % MOD)% MOD;
    return sum;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    vector<long long> a(n);
    vector<vector<long long>> tree(12, vector<long long>((n+1)*4,0));
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    update(tree[0], 0, n, 1, 0, 1);
    for (int i=0; i<n; i++){
        for (int j=1; j<=11; j++){
            long long t = get_sum(tree[j-1], 0, n, 1, 0, a[i]-1, 0);
            update(tree[j], 0, n, 1, a[i], t % MOD);
        }
    }
    cout << tree[11][1];

    return 0;
}