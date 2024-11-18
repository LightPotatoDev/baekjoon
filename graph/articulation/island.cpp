#include <iostream>
#include <vector>
#include <stack>
#include <set>
#include <algorithm>

using namespace std;

struct Node {
    int node_id;
    vector<pair<int, int>> coords;
    vector<int> connection;
    bool is_land;
    int depth;
    int visit_order;
    int low;
    bool safe;

    Node(int id, vector<pair<int, int>> coords_, bool is_land_) 
        : node_id(id), coords(coords_), is_land(is_land_), depth(0), visit_order(0), low(0), safe(true) {}
};

int n, m;
vector<vector<char>> grid;
vector<vector<int>> grid_visited;
vector<Node> nodes;
int assign_node_id = 0;

vector<int> dy = {0, -1, 0, 1};
vector<int> dx = {1, 0, -1, 0};
int visit_time = 1;

void assign_node(int y, int x, char icon) {
    stack<pair<int, int>> to_visit;
    vector<pair<int, int>> coords;

    to_visit.push({y, x});

    while (!to_visit.empty()) {
        int i = to_visit.top().first;
        int j = to_visit.top().second;
        to_visit.pop();

        coords.push_back({i, j});
        grid_visited[i][j] = assign_node_id;

        for (int d = 0; d < 4; ++d) {
            int ny = i + dy[d];
            int nx = j + dx[d];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid_visited[ny][nx] == -1 && grid[ny][nx] == icon) {
                to_visit.push({ny, nx});
                grid_visited[ny][nx] = assign_node_id;
            }
        }
    }

    nodes.emplace_back(assign_node_id, coords, icon == '#');
    assign_node_id++;
}

void dfs(int u, int par, int depth) {
    nodes[u].depth = depth;
    nodes[u].visit_order = visit_time;
    nodes[u].low = visit_time;
    visit_time++;

    for (int v : nodes[u].connection) {
        if (nodes[v].visit_order == 0) {
            dfs(v, u, depth + 1);
            nodes[u].low = min(nodes[u].low, nodes[v].low);
        } else if (v != par) {
            nodes[u].low = min(nodes[u].low, nodes[v].visit_order);
        }
    }
}

void mark_unsafe(int start_id) {
    stack<int> to_visit;
    to_visit.push(start_id);

    while (!to_visit.empty()) {
        int p = to_visit.top();
        to_visit.pop();

        nodes[p].safe = false;

        for (int v : nodes[p].connection) {
            if (nodes[v].safe && nodes[v].depth - nodes[p].depth == 1) {
                to_visit.push(v);
            }
        }
    }
}

int main() {
    cin >> n >> m;
    grid.resize(n, vector<char>(m));
    grid_visited.assign(n, vector<int>(m, -1));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid_visited[i][j] == -1) {
                assign_node(i, j, grid[i][j]);
            }
        }
    }


    for (Node &no : nodes) {
        for (const pair<int,int>&coord : no.coords) {
            int y = coord.first;
            int x = coord.second;
            for (int d = 0; d < 4; ++d) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid_visited[ny][nx] != no.node_id) {
                    no.connection.push_back(grid_visited[ny][nx]);
                }
            }
        }
        set<int> unique_connections(no.connection.begin(), no.connection.end());
        no.connection.assign(unique_connections.begin(), unique_connections.end());
    }

    dfs(0, -1, 1);

    for (Node &no : nodes) {
        if (no.is_land && no.safe == true) {
            for (int near : no.connection) {
                if (nodes[near].depth - no.depth == 1 && nodes[near].low >= no.visit_order && nodes[near].safe == true) {
                    mark_unsafe(near);
                }
            }
        }
    }

    for (Node &no : nodes) {
        if (no.is_land) {
            for (const pair<int,int>&coord : no.coords) {
                int y = coord.first;
                int x = coord.second;
                grid[y][x] = no.safe ? 'O' : 'X';
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << grid[i][j];
        }
        cout << "\n";
    }

    return 0;
}
