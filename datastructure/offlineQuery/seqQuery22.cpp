#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n = 0;
int two_query = 0;
vector<long long> a;
vector<long long> tree;
vector<long long> ans;

struct QueryOne{
    int pos;
    int val;
};
struct QueryTwo{
    int idx;
    int one_q;
    int left;
    int right;
};

bool cmp_q2(const QueryTwo &a, const QueryTwo &b){
    return a.one_q < b.one_q;
}

ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        out << i << ' ';
    }
    out << '\n';
    return out;
}

ostream& operator << (ostream& out, const vector<QueryOne>& v){
    for (QueryOne i : v){
        out << i.pos <<  ' ' << i.val << " / ";
    }
    out << '\n';
    return out;
}

ostream& operator << (ostream& out, const vector<QueryTwo>& v){
    for (QueryTwo i : v){
        out << i.idx << ' ' << i.one_q << ' ' << i.left << ' ' << i.right << " / ";
    }
    out << '\n';
    return out;
}

void tree_init(vector<long long>& a, vector<long long>& tree, int start=0, int end=n-1, int node=1){
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

void print_tree(){
    for (int i=0; i<n; i++){
        cout << get_sum(i,i) << ' ';
    }
    cout << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    tree.resize(n*4);
    a.resize(n);
    for (int i=0; i < n; i++){
        cin >> a[i];
    }
    tree_init(a, tree);
    
    int m;
    vector<QueryOne> q_ones;
    vector<QueryTwo> q_twos;
    cin >> m;
    for (int i=0; i<m; i++){
        int q;
        cin >> q;
        if (q == 1){
            int p, v;
            cin >> p >> v;
            q_ones.push_back({p-1,v});
        }
        else if (q == 2){
            int k, l, r;
            cin >> k >> l >> r;
            q_twos.push_back({two_query, k, l-1, r-1});
            two_query += 1;
        }
    }

    ans.resize(q_twos.size());
    sort(q_twos.begin(), q_twos.end(), cmp_q2);
    
    int cur = 0;
    for (QueryTwo q: q_twos){
        while(q.one_q > cur){
            update(q_ones[cur].pos, q_ones[cur].val - a[q_ones[cur].pos]);
            a[q_ones[cur].pos] = q_ones[cur].val;
            cur += 1;
        }
        ans[q.idx] = get_sum(q.left, q.right);
    }

    for (long long i: ans){
        cout << i << '\n';
    }

    return 0;
}