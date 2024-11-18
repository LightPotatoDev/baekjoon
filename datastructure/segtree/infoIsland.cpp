#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> tree;
int MOD = 1e9 + 7;
int n;

ostream& operator << (ostream& out, const vector<int>& v){
    for (int i : v){
        out << i << ' ';
    }
    out << '\n';
    return out;
}

ostream &operator<<(ostream &out, const vector<pair<int, int>> &v)
{
    for (pair<int, int> i : v)
    {
        out << i.first << ' ' << i.second << '\n';
    }
    out << '\n';
    return out;
}

void update(int pos, int add, int start = 0, int end = 4e5, int node = 1)
{
    if (!(start <= pos && pos <= end))
        return;
    tree[node] += add;
    if (start == end)
        return;
    int mid = (start + end) / 2;
    update(pos, add, start, mid, node * 2);
    update(pos, add, mid + 1, end, node * 2 + 1);
}

bool cmp_coords_y(const pair<int, int> &a, const pair<int, int> &b)
{
    if (a.second != b.second)
        return a.second > b.second;
    return a.first < b.first;
}

long long get_sum(int left, int right, long long sum = 0, int start = 0, int end = 4e5, int node = 1)
{
    if (left > end || right < start)
    {
        return 0;
    }
    if (left <= start && end <= right)
    {
        return tree[node];
    }
    int mid = (start + end) / 2;
    sum = get_sum(left, right, sum, start, mid, node * 2) + get_sum(left, right, sum, mid + 1, end, node * 2 + 1);
    return sum;
}

void print_tree(vector<long long> &tree)
{
    cout << "Tree printing" << endl;
    for (int i = 0; i < tree.size(); i++)
    {
        cout << tree[i] << endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    tree.resize((4e5+1) * 4);
    fill(tree.begin(), tree.end(), 0);
    vector<pair<int, int>> coords;
    coords.resize(n);
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        coords[i].first = x+2e5;
        coords[i].second = y;
    }

    sort(coords.begin(), coords.end(), cmp_coords_y);

    long long ans = 0;
    int prev_y = -2e5-1;
    vector<int> to_update;
    for (int i = 0; i < n; i++)
    {
        int x = coords[i].first;
        int y = coords[i].second;

        if (y != prev_y){
            for (int j : to_update){
                update(j,1);
            }
            to_update.resize(0);
        }

        long long s_left = get_sum(0, x-1);
        long long s_right = get_sum(x+1, 4e5);
        ans = (ans + (s_left * s_right) % MOD) % MOD;
        to_update.push_back(x);
        prev_y = y;
    }
    cout << ans;

    return 0;
}