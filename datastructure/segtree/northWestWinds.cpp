#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> tree;
int n;

ostream& operator << (ostream& out, const vector<pair<int,int>>& v){
    for (pair<int,int> i : v){
        out << i.first << ' ' << i.second << '\n';
    }
    out << '\n';
    return out;
}

void update(int pos, int add, int start = 0, int end = n-1, int node = 1){
    if (!(start <= pos && pos <= end)) return;
    tree[node] += add;
    if (start == end) return;
    int mid = (start+end)/2;
    update(pos, add, start, mid, node*2);
    update(pos, add, mid+1, end, node*2+1);
}

bool cmp_coords(const pair<int,int> &a, const pair<int,int> &b) {
    if (a.first != b.first)
        return a.first < b.first;
    return a.second < b.second;
}

bool cmp_coords_y(const pair<int,int> &a, const pair<int,int> &b) {
    if (a.second != b.second)
        return a.second > b.second;
    return a.first < b.first;
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
    
    int t;
    cin >> t;

    for (int tc=0; tc < t; tc++){
        cin >> n;
        tree.resize(n*4);
        fill(tree.begin(), tree.end(), 0);
        vector<pair<int,int>> coords;
        coords.resize(n);
        for (int i=0; i<n; i++){
            int x,y;
            cin >> x >> y;
            coords[i].first = x;
            coords[i].second = y;
        }

        sort(coords.begin(), coords.end(), cmp_coords_y);
        for (int i=0; i<n; i++){
            coords[i].second = i;
        }
        sort(coords.begin(), coords.end(), cmp_coords);
        long long ans = 0;
        for (int i=0; i<n; i++){
            int y = coords[i].second;
            ans += get_sum(0,y);
            update(y,1);
        }
        cout << ans << '\n';

    }

    return 0;
}