#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int MAX=100002;
vector<long long> lazy(MAX*4);
vector<long long> tree(MAX*4);

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

void update_lazy(int start, int end, int node){
    if (lazy[node] != 0){
        tree[node] += lazy[node] * (end-start+1);
        if (start != end){
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update_range(int left, int right, long long add, int start=0, int end=MAX-1, int node = 1){
    //start, end - 현재 노드의 배열 범위 
    //left, right - 업데이트 범위
    update_lazy(start, end, node);
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
    update_range(left, right, add, start, mid, node*2);
    update_range(left, right, add, mid+1, end, node*2+1);
    tree[node] = tree[node*2] + tree[node*2+1];
}

long long get_sum(int left, int right, long long sum=0, int start=0, int end=MAX-1, int node=1){
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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    for (int tc=0; tc<t; tc++){
        int n,m,ans;
        ans = 0;
        cin >> n >> m;

        vector<vector<int>> coords(MAX);
        vector<vector<vector<int>>> queries(MAX); // [l,r,add]
        fill(tree.begin(), tree.end(), 0);
        fill(lazy.begin(), lazy.end(), 0);
        
        for (int i=0; i<n; i++){
            int a,b;
            cin >> a >> b;
            coords[a].push_back(b);
        }
        for (int i=0; i<m; i++){
            int l,r,b,t;
            cin >> l >> r >> b >> t;
            queries[l].push_back({b,t,1});
            queries[r+1].push_back({b,t,-1});
        }

        for (int i=0; i<MAX; i++){
            for (vector<int> q:queries[i]){
                int b,t,add;
                b = q[0];
                t = q[1];
                add = q[2];
                update_range(b,t,add);
            }
            for (int y:coords[i]){
                ans += get_sum(y,y);
            }
        }

        cout << ans << '\n';
    }

    return 0;
}