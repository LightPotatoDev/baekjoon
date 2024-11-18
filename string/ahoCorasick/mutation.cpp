#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
using namespace std;

map<char,int> dna = {{'A',0}, {'G',1}, {'T', 2}, {'C',3}};
vector<char> dna_rev = {'A', 'G', 'T', 'C'};
const int CHAR_NUM = 4;

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
            return;
        }

        int c = dna[str[idx]];
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
                    trie[nxt].valid = true;

                q.push(nxt);
            }
        }
    }

    int search(string &s)
    {
        int cur = 0;
        int cnt = 0;
        for (auto &x : s)
        {
            int nxt = dna[x];
            while (cur != 0 && trie[cur].child[nxt] == -1)
                cur = trie[cur].fail;
            if (trie[cur].child[nxt] != -1)
                cur = trie[cur].child[nxt];
            if (trie[cur].valid)
                cnt += 1;
        }
        return cnt;
    }

    void print(){
        for (int i = 0; i<trie.size(); i++){
            Node node = trie[i];
            cout << "Node " << i << ":\nChild: ";
            for (int j = 0; j < CHAR_NUM; j++){
                if (node.child[j] != -1){
                    char c = dna_rev[j];
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

vector<string> make_mutation(string s){
    vector<string> mutation = {s};
    int n = s.size();

    for (int i=0; i<n-1; i++){
        for (int j=i+1; j<n; j++){
            reverse(s.begin()+i, s.begin()+j+1);
            mutation.push_back(s);
            reverse(s.begin()+i, s.begin()+j+1);
        }
    }

    return mutation;
}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++){
        int n,m; 
        cin >> n >> m;
        string s,t;
        cin >> s >> t;

        vector<string> search_set = make_mutation(t);

        AhoCorasick aho(search_set);
        cout << aho.search(s) << '\n';
        
    }

    return 0;
}