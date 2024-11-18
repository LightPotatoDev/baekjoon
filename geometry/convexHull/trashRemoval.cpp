#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>
#include <iomanip>
using namespace std;

struct Point
{
    long long x, y;
    bool operator<(const Point &a)
    {
        if (y == a.y)
            return x < a.x;
        return y < a.y;
    }
};
vector<Point> points;

long long ccw(const Point &a, const Point &b, const Point &c)
{
    return a.x * b.y + b.x * c.y + c.x * a.y - a.y * b.x - b.y * c.x - c.y * a.x;
}

long long dist(const Point &a, const Point &b)
{
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

bool ccw_cmp(const Point &a, const Point &b)
{
    long long c = ccw(points[0], a, b);

    if (c == 0)
        return dist(points[0], a) < dist(points[0], b);
    return c > 0;
}

vector<long long> line_equation(const Point &a, const Point &b)
{
    return {(b.y - a.y), -(b.x - a.x), (b.x - a.x) * a.y - (b.y - a.y) * a.x};
}

double line_point_dist(const vector<long long> &line, const Point &p)
{
    return abs(line[0] * p.x + line[1] * p.y + line[2]) / sqrt(line[0] * line[0] + line[1] * line[1]);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t = 0;
    while (true)
    {
        int n;
        cin >> n;
        if (n == 0)
            break;

        t += 1;
        points.resize(n);
        for (int i = 0; i < n; i++)
        {
            long long x, y;
            cin >> x >> y;
            points[i].x = x;
            points[i].y = y;
        }

        sort(points.begin(), points.end());
        sort(points.begin() + 1, points.end(), ccw_cmp);
        double ans = 1e9;

        stack<Point> stk;
        stk.push(points[0]);
        stk.push(points[1]);

        for (int i = 2; i < n; i++)
        {
            while (stk.size() >= 2)
            {
                Point p1 = stk.top();
                stk.pop();
                Point p2 = stk.top();
                if (ccw(p2, p1, points[i]) > 0)
                {
                    stk.push(p1);
                    break;
                }
            }
            stk.push(points[i]);
        }

        vector<Point> convex_points(stk.size());
        int nn = stk.size();
        for (int i = stk.size()-1; i >= 0; i--){
            convex_points[i] = stk.top();
            stk.pop();
        }

        for (int i = 0; i < nn; i++)
        {
            int p1, p2;
            p1 = i;
            p2 = i + 1;
            if (i == nn - 1)
                p2 = 0;
            double max_dist = 0;
            vector<long long> line = line_equation(convex_points[p1], convex_points[p2]);
            for (int j = 0; j < nn; j++)
            {
                max_dist = max(max_dist, line_point_dist(line, convex_points[j]));
            }
            ans = min(ans, max_dist);
        }

        cout << "Case " << t << ": " << fixed << setprecision(2) << ceil(ans * 100.0) / 100.0 << '\n';
    }
}