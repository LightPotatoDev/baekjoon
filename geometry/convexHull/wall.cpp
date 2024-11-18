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

double angle(const Point &a, const Point &b, const Point &c)
{
    Point u = {b.x - a.x, b.y - a.y};
    Point v = {c.x - b.x, c.y - b.y};
    return acos((u.x * v.x + u.y * v.y) / (sqrt(dist(a, b)) * sqrt(dist(b, c))));
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n,l;
    cin >> n >> l;

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
    double ans = 0;

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
    for (int i = stk.size() - 1; i >= 0; i--)
    {
        convex_points[i] = stk.top();
        stk.pop();
    }

    for (int i = 0; i < nn; i++)
    {
        ans += sqrt(dist(convex_points[i%nn], convex_points[(i+1)%nn]));
        ans += angle(convex_points[i%nn], convex_points[(i+1)%nn], convex_points[(i+2)%nn]) * l;
    }

    cout << round(ans);
}