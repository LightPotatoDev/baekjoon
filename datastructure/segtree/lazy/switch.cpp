#include <iostream>
#include <vector>
using namespace std;

void update_lazy(vector<long long>& tree, vector <long long>& lazy, int start, int end, int node){
    if (lazy[node] != 0){
        tree[node] = (end-start+1) - tree[node];
        if (start != end){
            lazy[node*2] = (lazy[node] + lazy[node*2])%2;
            lazy[node*2+1] = (lazy[node] + lazy[node*2+1])%2;
        }
        lazy[node] = 0;
    }
}

void update_range(vector<long long>& tree, vector<long long>& lazy, int start, int end, int node, int left, int right){
    //start, end - 현재 노드의 배열 범위 
    //left, right - 업데이트 범위
    update_lazy(tree, lazy, start, end, node);
    if (left > end || right < start){
        return;
    }
    if (left <= start && end <= right){
        tree[node] = (end-start+1) - tree[node];
        if (start != end){
            lazy[node*2] = (lazy[node*2] + 1)%2;
            lazy[node*2+1] = (lazy[node*2+1] + 1)%2;
        }
        return;
    }
    int mid = (start+end)/2;
    update_range(tree, lazy, start, mid, node*2, left, right);
    update_range(tree, lazy, mid+1, end, node*2+1, left, right);
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
    cin >> n >> m;
    vector<long long> a(n,0);
    vector<long long> tree(n*4,0);
    vector<long long> lazy(n*4,0);

    for (int i=0; i<m; i++){
        int q, left, right;
        cin >> q >> left >> right;
        if (q == 0){
            update_range(tree, lazy, 0, n-1, 1, left-1, right-1);
            //print_tree(tree, lazy);
        }
        else if (q == 1)
        {
            cout << get_sum(tree, lazy, 0, n-1, 1, left-1, right-1, 0) << '\n';
        }
        
    }

    return 0;
}