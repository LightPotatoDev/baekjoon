#include <iostream>
#include <vector>
using namespace std;

void update(vector<long long>& tree, int start, int end, int node, int pos, long long add){
    if (!(start <= pos && pos <= end)) return;
    tree[node] += add;
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
    sum = get_sum(tree, start, mid, node*2, left, right, sum) + get_sum(tree, mid+1, end, node*2+1, left, right, sum);
    return sum;
}

const long long MOD = 1000000007;

long long perm(long long n, long long k) {
    long long res = 1;
    for (int i = n; i > n - k; --i) {
        res = (res * i) % MOD;
    }
    return res;
}

long long pow(long long n, long long k) {
    long long res = 1;
    while (k > 0) {
        if (k % 2 == 1) {
            res = (res * n) % MOD;
        }
        n = (n * n) % MOD;
        k /= 2;
    }
    return res;
}

long long comb(long long n, long long k){
    return (perm(n, k) * pow(perm(k, k), MOD - 2)) % MOD;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,k;
    cin >> n >> k;
    long long ans = 0;
    vector<long long> a(n);
    vector<long long> tree(n*4);
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    for (int i=0; i<n; i++){
        update(tree,0,n-1,1,a[i]-1,1);
        long long lowers = get_sum(tree, 0, n-1, 1, 0, a[i]-2, 0);
        ans = (ans + comb(lowers, k-1)) % MOD;
    }
    cout << ans;

    return 0;
}