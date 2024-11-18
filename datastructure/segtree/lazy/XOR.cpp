#include <iostream>
#include <vector>
using namespace std;

void tree_init(vector<long long>& a, vector<long long>& tree, int start, int end, int node){
    if (start == end){
        tree[node] = a[start];
        return;
    }
    int mid = (start+end) / 2;
    tree_init(a,tree,start,mid,node*2);
    tree_init(a,tree,mid+1,end,node*2+1);
    tree[node] = tree[node*2] ^ tree[node*2+1];
    return;
}

void update_lazy(vector<long long>& tree, vector <long long>& lazy, int start, int end, int node){
    if (lazy[node] != 0){
        if ((end-start+1)%2 == 1)
            tree[node] ^= lazy[node];
        if (start != end){
            lazy[node*2] ^= lazy[node];
            lazy[node*2+1] ^= lazy[node];
        }
        lazy[node] = 0;
    }
}

void update_range(vector<long long>& tree, vector<long long>& lazy, int start, int end, int node, int left, int right, int k){
    //start, end - 현재 노드의 배열 범위 
    //left, right - 업데이트 범위
    update_lazy(tree, lazy, start, end, node);
    if (left > end || right < start){
        return;
    }
    if (left <= start && end <= right){
        if ((end-start+1)%2 == 1)
            tree[node] = k ^ tree[node];
        if (start != end){
            lazy[node*2] ^= k;
            lazy[node*2+1] ^= k;
        }
        return;
    }
    int mid = (start+end)/2;
    update_range(tree, lazy, start, mid, node*2, left, right, k);
    update_range(tree, lazy, mid+1, end, node*2+1, left, right, k);
    tree[node] = tree[node*2] ^ tree[node*2+1];
}

long long get_xor(vector<long long>& tree, vector<long long>& lazy, int start, int end, int node, int left, int right, long long _xor){
    update_lazy(tree, lazy, start, end, node);
    if (left > end || right < start){
        return 0;
    }
        if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start+end)/2;
    _xor = get_xor(tree, lazy, start, mid, node*2, left, right, _xor) ^ get_xor(tree, lazy, mid+1, end, node*2+1, left, right, _xor);
    return _xor;
}

void print_tree(vector<long long>& tree, vector<long long>& lazy){
    cout << "Tree printing" << endl;
    for (int i=0; i<tree.size(); i++){
        cout << "Num: " << i << " Tree: "<< tree[i]  << " Lazy: " << lazy[i] << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,m;
    cin >> n;
    vector<long long> a(n,0);
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    cin >> m;
    vector<long long> tree(n*4,0);
    vector<long long> lazy(n*4,0);
    tree_init(a,tree,0,n-1,1);

    for (int i=0; i<m; i++){
        int q, left, right, k;
        cin >> q;
        if (q == 1){
            cin >> left >> right >> k;
            update_range(tree, lazy, 0, n-1, 1, left, right, k);
        }
        else if (q == 2)
        {
            cin >> left >> right;
            cout << get_xor(tree, lazy, 0, n-1, 1, left, right, 0) << '\n';
        }
        //print_tree(tree, lazy);
    }

    return 0;
}