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
    tree[node] = tree[node*2] + tree[node*2+1];
    return;
}

void update_lazy(vector<long long>& tree, vector <long long>& lazy, int start, int end, int node){
    if (lazy[node] != 0){
        tree[node] += lazy[node] * (end-start+1);
        if (start != end){
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update_range(vector<long long>& tree, vector<long long>& lazy, int start, int end, int node, int left, int right, long long add){
    //start, end - 현재 노드의 배열 범위 
    //left, right - 업데이트 범위
    update_lazy(tree, lazy, start, end, node);
    if (left > end || right < start){
        return;
    }
    if (left <= start && end <= right){
        tree[node] += add * (end-start+1);
        if (start != end){
            lazy[node*2] += add;
            lazy[node*2+1] += add;
        }
        return;
    }
    int mid = (start+end)/2;
    update_range(tree, lazy, start, mid, node*2, left, right, add);
    update_range(tree, lazy, mid+1, end, node*2+1, left, right, add);
    tree[node] = tree[node*2] + tree[node*2+1];
}

long long get_sum(vector<long long>& tree, vector<long long>& lazy, int start, int end, int node, int left, int right, long long sum){
    update_lazy(tree, lazy, start, end, node);
    if (left > end || right < start){
        return 0;
    }
        if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start+end)/2;
    sum = get_sum(tree, lazy, start, mid, node*2, left, right, sum) + get_sum(tree, lazy, mid+1, end, node*2+1, left, right, sum);
    return sum;
}

void print_tree(vector<long long>& tree){
    cout << "Tree printing" << endl;
    for (int i=0; i<tree.size() * 4; i++){
        cout << tree[i] << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,m,k;
    cin >> n >> m >> k;
    vector<long long> a(n);
    vector<long long> tree(n*4);
    vector<long long> lazy(n*4);
    fill(tree.begin(), tree.end(), 0);
    fill(lazy.begin(), lazy.end(), 0);
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    tree_init(a,tree,0,n-1,1);
    for (int i=0; i<m+k; i++){
        int q;
        cin >> q;
        int left, right;
        if (q == 1){
            long long add;
            cin >> left >> right >> add;
            update_range(tree, lazy, 0, n-1, 1, left-1, right-1, add);
        }
        else if (q == 2)
        {
            cin >> left >> right;
            cout << get_sum(tree, lazy, 0, n-1, 1, left-1, right-1, 0) << '\n';
        }
        
    }

    return 0;
}