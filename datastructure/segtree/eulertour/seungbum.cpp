#include <iostream>
#include <vector>
using namespace std;

void dfs(vector<vector<int>>& graph, vector<int>& visited, vector<int>& finished, int& visit_ord, int u){
    visited[u] = visit_ord;
    visit_ord += 1;
    for (int v : graph[u]){
        if (visited[v] == -1)
            dfs(graph, visited, finished, visit_ord, v);
    }
    finished[u] = visit_ord-1;
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
    for (int i=0; i<tree.size(); i++){
        cout << tree[i] << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    vector<long long> a(n);
    vector<long long> tree(n*4);
    vector<long long> lazy(n*4);
    vector<int> visited(n,-1);
    vector<int> finished(n, -1);
    int visit_ord = 0;

    for (int i=0; i<n; i++){
        int v;
        cin >> v;
        if (v != -1){
            graph[v-1].push_back(i);
        }
    }

    dfs(graph, visited, finished, visit_ord, 0);

    for (int i=0; i<m; i++){
        int q;
        cin >> q;
        if (q == 1){
            int u,w;
            cin >> u >> w;
            update_range(tree, lazy, 0, n-1, 1, visited[u-1], finished[u-1], w);
        }
        else if (q == 2){
            int u;
            cin >> u;
            cout << get_sum(tree, lazy, 0, n-1, 1, visited[u-1], visited[u-1], 0) << '\n';
        }
    }
    

    return 0;
}