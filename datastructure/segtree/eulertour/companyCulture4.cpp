#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graph;
vector<int> visited;
vector<int> finished;
vector<long long> lazy;
vector<long long> lazy2;
vector<long long> tree_up;
vector<long long> tree_down;
int visit_ord = 0;
int n = 0;

ostream& operator << (ostream& out, const vector<long long>& v){
    for (int i : v){
        out << i << ' ';
    }
    out << '\n';
    return out;
}
ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        out << i << ' ';
    }
    out << '\n';
    return out;
}

void dfs(int u){
    visited[u] = visit_ord;
    visit_ord += 1;
    for (int v : graph[u]){
        if (visited[v] == -1)
            dfs(v);
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

void update_range(vector<long long>& tree, vector<long long>& lazy, int left, int right, long long add, int start=0, int end=n-1, int node = 1){
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
    update_range(tree, lazy, left, right, add, start, mid, node*2);
    update_range(tree, lazy, left, right, add, mid+1, end, node*2+1);
    tree[node] = tree[node*2] + tree[node*2+1];
}

long long get_sum(vector<long long>& tree, vector<long long>& lazy, int left, int right, long long sum=0, int start=0, int end=n-1, int node=1){
    update_lazy(tree, lazy, start, end, node);
    if (left > end || right < start){
        return 0;
    }
        if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start+end)/2;
    sum = get_sum(tree, lazy, left, right, sum, start, mid, node*2) + get_sum(tree, lazy, left, right, sum, mid+1, end, node*2+1);
    return sum;
}

void print_tree(vector<long long>& tree){
    for (int i=0; i<n; i++){
        cout << get_sum(tree, lazy, i, i) << ' ';
    }
    cout << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int m;
    cin >> n >> m;
    graph.resize(n);
    visited.resize(n);
    fill(visited.begin(), visited.end(), -1);
    finished.resize(n);
    lazy.resize(n*4);
    lazy2.resize(n*4);
    tree_up.resize(n*4);
    tree_down.resize(n*4);

    for (int i=0; i<n; i++){
        int u;
        cin >> u;
        if (u != -1){
            graph[u-1].push_back(i);
        }
    }

    dfs(0);
    bool going_up = false;

    for (int i=0; i<m; i++){
        int q, u, w;
        cin >> q;
        if (q == 1){
            cin >> u >> w;
            if (going_up)
                update_range(tree_up, lazy, visited[u-1], visited[u-1], w);
            else
                update_range(tree_down, lazy2, visited[u-1], finished[u-1], w);
        }
        else if (q == 2){
            cin >> u;
            cout << get_sum(tree_up, lazy, visited[u-1], finished[u-1]) + get_sum(tree_down, lazy2, visited[u-1], visited[u-1]) << '\n';
        }
        else if (q == 3){
            going_up = !going_up;
        }
    }
    return 0;
}