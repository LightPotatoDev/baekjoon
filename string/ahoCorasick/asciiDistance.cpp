#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

const int CHAR_NUM = 26;
const char MIN_CHAR = 'a';

class Node
{
private:
    bool valid; // 찾는 단어 중 하나?
    int length;
    vector<int> child;
    int fail;

public:
    Node()
    {
        valid = false;
        length = 0;
        fail = 0;
        child.resize(CHAR_NUM);
        fill(child.begin(), child.end(), -1);
    }
    friend class AhoCorasick;
};

class AhoCorasick
{
private:
    vector<Node> trie;

    int _new_node()
    {
        Node t;
        trie.push_back(t);
        return trie.size() - 1;
    }

    void _add(string &str, int node, int idx)
    {
        if (idx == str.size())
        {
            trie[node].valid = true;
            trie[node].length = max(trie[node].length, (int)str.size());
            return;
        }

        int c = str[idx] - MIN_CHAR;
        if (trie[node].child[c] == -1)
        {
            int next = _new_node();
            trie[node].child[c] = next;
        }

        _add(str, trie[node].child[c], idx + 1);
    }

public:
    AhoCorasick(vector<string> &search_set)
    {
        _new_node();

        for (auto &s : search_set)
            _add(s, 0, 0);

        queue<int> q;
        for (auto &x : trie[0].child)
        {
            if (x != -1)
            {
                q.push(x);
                trie[x].fail = 0;
            }
        }

        while (!q.empty())
        {
            int cur = q.front();
            q.pop();

            for (int i = 0; i < CHAR_NUM; i++)
            {
                int nxt = trie[cur].child[i];
                if (nxt == -1)
                    continue;

                int dest = trie[cur].fail;
                while (dest != 0 && trie[dest].child[i] == -1)
                    dest = trie[dest].fail;

                if (trie[dest].child[i] != -1)
                    dest = trie[dest].child[i];
                trie[nxt].fail = dest;

                if (trie[trie[nxt].fail].valid)
                {
                    trie[nxt].valid = true;
                    trie[nxt].length = max(trie[nxt].length, trie[trie[nxt].fail].length);
                }

                q.push(nxt);
            }
        }
    }

    vector<pair<int, int>> search(string &s)
    {
        int cur = 0;
        vector<pair<int, int>> found;
        for (int i = 0; i < s.size(); i++)
        {
            char x = s[i];
            int nxt = x - MIN_CHAR;
            while (cur != 0 && trie[cur].child[nxt] == -1)
                cur = trie[cur].fail;
            if (trie[cur].child[nxt] != -1)
                cur = trie[cur].child[nxt];
            if (trie[cur].valid)
            {
                found.push_back({i - trie[cur].length + 1, i});
            }
        }
        return found;
    }

    void print()
    {
        for (int i = 0; i < trie.size(); i++)
        {
            Node node = trie[i];
            cout << "Node " << i << ":\nChild: ";
            for (int j = 0; j < CHAR_NUM; j++)
            {
                if (node.child[j] != -1)
                {
                    char c = j + MIN_CHAR;
                    cout << c << '-' << node.child[j] << ' ';
                }
            }
            cout << '\n';
            cout << "Fail: " << node.fail << '\n';
            cout << "Valid: " << node.valid << '\n';
            cout << "Length: " << node.length << '\n';
            cout << '\n';
        }
    }
};

int find_distance(vector<pair<int, int>> &v)
{
    sort(v.begin(), v.end());
    int res = 0, l = -1, r = -2;
    for (int i = 0; i < v.size(); i++)
    {
        if (r < v[i].first)
        {
            res += r-l+1;
            l = v[i].first;
            r = v[i].second;
        }
        else
        {
            r = max(r, v[i].second);
        }
    }
    res += r-l+1;
    return res;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    string tiles;
    cin >> tiles;

    int m;
    cin >> m;
    vector<string> search_set(m);
    vector<pair<int,int>> found;
    for (int i = 0; i < m; i++)
    {
        cin >> search_set[i];
    }

    const int BATCH = 200;
    for (int i=0; i < m/BATCH+1; i++){
        vector<string> search_subset = vector<string>(search_set.begin()+i*BATCH, min(search_set.begin()+i*BATCH + BATCH,search_set.end()));
        AhoCorasick aho(search_subset);
        vector<pair<int, int>> found_t = aho.search(tiles);
        for (auto p:found_t){
            found.push_back(p);
        }
    }
    /*
    for (int i=0; i < found.size(); i++){
        cout << found[i].first << ' ' << found[i].second << '\n';
    }
    */
    cout << n - find_distance(found);

    return 0;
}