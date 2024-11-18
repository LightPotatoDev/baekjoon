#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Node
{
private:
    bool valid; // 찾는 단어 중 하나?
    vector<int> child;
    int fail;

public:
    Node()
    {
        valid = false;
        fail = 0;
        child.resize(26);
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
            return;
        }

        int c = str[idx] - 'a';
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

            for (int i = 0; i < 26; i++)
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
                    trie[nxt].valid = true;

                q.push(nxt);
            }
        }
    }

    bool search(string &s)
    {
        int cur = 0;
        for (auto &x : s)
        {
            int nxt = x-'a';
            while (cur != 0 && trie[cur].child[nxt] == -1)
                cur = trie[cur].fail;
            if (trie[cur].child[nxt] != -1)
                cur = trie[cur].child[nxt];
            if (trie[cur].valid)
                return true;
        }
        return false;
    }

    void print(){
        for (int i = 0; i<trie.size(); i++){
            Node node = trie[i];
            cout << "Node " << i << ":\nChild: ";
            for (int j = 0; j < 26; j++){
                if (node.child[j] != -1){
                    char c = j + 'a';
                    cout << c << '-' << node.child[j] << ' ';
                }
            }
            cout << '\n';
            cout << "Fail: " << node.fail << '\n';
            cout << "Valid: " << node.valid << '\n';
            cout << '\n';
        }
    }
};

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<string> search_set;
    for (int i=0; i<n; i++){
        string s;
        cin >> s;
        search_set.push_back(s);
    }
    AhoCorasick aho(search_set);

    int q;
    cin >> q;
    for (int i=0; i<q; i++){
        string s;
        cin >> s;
        bool res = aho.search(s);
        if (res)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}