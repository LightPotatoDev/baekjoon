#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <bitset>
#include <unordered_map>
using namespace std;

const int CHAR_NUM = 2;
const int BIT_LEN = 32;
const char MIN_CHAR = '0';

class Node
{
private:
    bool valid;
    vector<int> child;
    vector<bool> valid_child;

public:
    Node()
    {
        valid = false;
        child.resize(CHAR_NUM);
        valid_child.resize(CHAR_NUM);
        fill(child.begin(), child.end(), -1);
    }
    friend class Trie;
};

class Trie
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

        int c = str[idx] - MIN_CHAR;
        if (trie[node].child[c] == -1)
        {
            int next = _new_node();
            trie[node].child[c] = next;
        }
        trie[node].valid_child[c] = true;

        _add(str, trie[node].child[c], idx + 1);
    }

public:
    Trie()
    {
        _new_node();
    }

    void add(string &s)
    {
        _add(s, 0, 0);
    }

    void remove(string &s)
    {
        vector<pair<int,int>> to_remove;
        int cur = 0;

        for (auto &x:s){

            if (trie[cur].valid_child[0] == true && trie[cur].valid_child[1] == true)
                to_remove.clear();

            int c = x - MIN_CHAR;
            to_remove.push_back({cur,c});
            cur = trie[cur].child[c];
        }

        for (auto &p:to_remove){
            trie[p.first].valid_child[p.second] = false;
        }
    }

    long long search(string &s)
    {
        int cur = 0;
        long long res = 0;
        for (auto &x:s){
            x = x-MIN_CHAR;
            int rx = 1-x;
            if (trie[cur].valid_child[rx]){
                cur = trie[cur].child[rx];
                res += 1;
            }
            else{
                cur = trie[cur].child[x];
            }
            res <<= 1;
        }
        res >>= 1;
        return res;
    }

    void print()
    {
        for (int i = 0; i < trie.size(); i++)
        {
            Node node = trie[i];
            cout << "Node " << i << ":\nChild: ";
            for (int j = 0; j < CHAR_NUM; j++)
            {
                if (node.child[j] != -1 && node.valid_child[j] == true)
                {
                    char c = j + MIN_CHAR;
                    cout << c << '-' << node.child[j] << ' ';
                }
            }
            cout << '\n';
            cout << "Valid: " << node.valid << '\n';
            cout << '\n';
        }
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    Trie trie;
    unordered_map<int,int> used;
    string bzero = bitset<BIT_LEN>(0).to_string();
    trie.add(bzero);
    for (int i = 0; i < n; i++)
    {
        int q, x;
        cin >> q >> x;

        string bx = bitset<BIT_LEN>(x).to_string();
        if (q == 1){
            trie.add(bx);
            if (used.count(x) > 0)
                used[x] += 1;
            else
                used[x] = 1;
        }
        else if (q == 2){
            used[x] -= 1;
            if (used[x] == 0)
                trie.remove(bx);
        }
        else if (q == 3)
            cout << trie.search(bx) << '\n';
    }

    return 0;
}