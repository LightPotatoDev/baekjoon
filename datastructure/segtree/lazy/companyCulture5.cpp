#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graph;
vector<int> visited;
vector<int> finished;
vector<long long> lazy;
vector<long long> tree;
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

void update_lazy(int start, int end, int node){
    if (lazy[node] != -1){
        tree[node] = lazy[node] * (end-start+1);
        if (start != end){
            lazy[node*2] = lazy[node];
            lazy[node*2+1] = lazy[node];
        }
        lazy[node] = -1;
    }
}

void update_range(int left, int right, long long set, int start=0, int end=n-1, int node = 1){
    //start, end - 현재 노드의 배열 범위 
    //left, right - 업데이트 범위
    update_lazy(start, end, node);
    if (left > end || right < start){
        return;
    }
    if (left <= start && end <= right){
        tree[node] = set * (end-start+1);
        if (start != end){
            lazy[node*2] = set;
            lazy[node*2+1] = set;
        }
        return;
    }
    int mid = (start+end)/2;
    update_range(left, right, set, start, mid, node*2);
    update_range(left, right, set, mid+1, end, node*2+1);
    tree[node] = tree[node*2] + tree[node*2+1];
}

long long get_sum(int left, int right, long long sum=0, int start=0, int end=n-1, int node=1){
    update_lazy(start, end, node);
    if (left > end || right < start){
        return 0;
    }
        if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start+end)/2;
    sum = get_sum(left, right, sum, start, mid, node*2) + get_sum(left, right, sum, mid+1, end, node*2+1);
    return sum;
}

void print_tree(vector<long long>& tree){
    for (int i=0; i<n; i++){
        cout << get_sum(i, i) << ' ';
    }
    cout << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    graph.resize(n);
    visited.resize(n);
    fill(visited.begin(), visited.end(), -1);
    finished.resize(n);
    lazy.resize(n*4);
    fill(lazy.begin(), lazy.end(), -1);
    tree.resize(n*4);

    for (int i=0; i<n; i++){
        int u;
        cin >> u;
        if (u != 0){
            graph[u-1].push_back(i);
        }
    }

    dfs(0);
    update_range(visited[0], finished[0], 1);
    
    int m;
    cin >> m;

    for (int i=0; i<m; i++){
        int q, u;
        cin >> q >> u;
        if (q == 1){
            int prev_state = get_sum(visited[u-1], visited[u-1]);
            update_range(visited[u-1], finished[u-1], 1);
            update_range(visited[u-1], visited[u-1], prev_state);
        }
        else if (q == 2){
            int prev_state = get_sum(visited[u-1], visited[u-1]);
            update_range(visited[u-1], finished[u-1], 0);
            update_range(visited[u-1], visited[u-1], prev_state);
        }
        else if (q == 3){
            cout << get_sum(visited[u-1], finished[u-1]) - get_sum(visited[u-1], visited[u-1]) << '\n';
        }
    }

    return 0;
}