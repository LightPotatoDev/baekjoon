#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graph;
vector<int> visited;
vector<int> finished;
vector<int> depths;
vector<long long> tree;
int visit_ord = 0;
int n = 0;

ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        out << i << ' ';
    }
    out << '\n';
    return out;
}

void dfs(int u, int depth){
    visited[u] = visit_ord;
    visit_ord += 1;
    for (int v : graph[u]){
        if (visited[v] == -1)
            dfs(v, depth+1);
    }
    depths[u] = depth;
    finished[u] = visit_ord-1;
}

void update(int pos, int add, int start = 0, int end = n-1, int node = 1){
    if (!(start <= pos && pos <= end)) return;
    tree[node] += add;
    if (start == end) return;
    int mid = (start+end)/2;
    update(pos, add, start, mid, node*2);
    update(pos, add, mid+1, end, node*2+1);
}


long long get_sum(int left, int right, long long sum=0, int start=0, int end=n-1, int node=1){
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
    cout << "Tree printing" << endl;
    for (int i=0; i<tree.size(); i++){
        cout << tree[i] << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int c;
    cin >> n >> c;
    graph.resize(n);
    visited.resize(n);
    fill(visited.begin(), visited.end(), -1);
    finished.resize(n);
    depths.resize(n);
    tree.resize(n*4);

    for (int i=0; i<n-1; i++){
        int u,v;
        cin >> u >> v;
        graph[u-1].push_back(v-1);
        graph[v-1].push_back(u-1);
    }

    dfs(c-1,1);
    
    int m;
    cin >> m;
    for (int i=0; i<m; i++){
        int q, u;
        cin >> q >> u;
        if (q == 1){
            update(visited[u-1], 1);
        }
        else if (q == 2){
            cout << get_sum(visited[u-1], finished[u-1]) * depths[u-1] << '\n';
        }
    }

    return 0;
}