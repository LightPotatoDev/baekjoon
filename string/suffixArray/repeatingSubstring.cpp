#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

ostream &operator<<(ostream &out, const vector<int> &v)
{
    for (int i : v)
    {
        out << i << ' ';
    }
    return out;
}

vector<int> sa;  // suffix array
vector<int> pos; // group number
vector<int> lcp;
void make_suffix_array(string s)
{

    int n = s.size();
    int d = 1;

    for (int i = 0; i < n; i++)
    {
        sa[i] = i;
        pos[i] = s[i];
    }

    auto cmp = [&](int i, int j) -> bool
    {
        if (pos[i] != pos[j])
            return pos[i] < pos[j];

        i += d;
        j += d;
        if (i < n && j < n)
            return pos[i] < pos[j];
        else
            return i > j;
    };

    for (d = 1;; d *= 2)
    {
        sort(sa.begin(), sa.end(), cmp);
        vector<int> tmp(n);

        for (int i = 0; i < n - 1; i++)
        {
            tmp[i + 1] = tmp[i] + cmp(sa[i], sa[i + 1]);
        }
        for (int i = 0; i < n; i++)
        {
            pos[sa[i]] = tmp[i];
        }

        if (tmp[n - 1] == n - 1)
            break;
    }
}

void make_lcp_array(string s)
{
    int n = s.size();
    for (int i = 0, k = 0; i < n; i++, k = max(k - 1, 0))
    {
        if (pos[i] == 0)
            continue;

        for (int j = sa[pos[i] - 1]; s[i + k] == s[j + k]; k++)
            ;

        lcp[pos[i]] = k;
    }
}

void print_lcp_array(string s)
{
    int n = s.size();
    vector<string> st(n);
    for (int i = 0; i < n; i++)
    {
        st[pos[i]] = s.substr(i, n - i);
    }
    for (int i = 0; i < n; i++)
    {
        cout << st[i] << string(sa[i] + 1, ' ') << lcp[i] << '\n';
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++)
    {
        string s;
        cin >> s;
        int n = s.size();
        sa.resize(n);
        pos.resize(n);
        lcp.resize(n);

        make_suffix_array(s);
        make_lcp_array(s);
        
        long long ans = 0;
        for (int i=0; i<n-1; i++){
            ans += max(0, lcp[i+1] - lcp[i]);
        }
        cout << ans << '\n';
    }
    return 0;
}