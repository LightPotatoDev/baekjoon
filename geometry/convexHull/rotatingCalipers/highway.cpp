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

long long ccw(Point a, Point b, Point c)
{
    return a.x * b.y + b.x * c.y + c.x * a.y - a.y * b.x - b.y * c.x - c.y * a.x;
}

long long cccw(Point a, Point b, Point c, Point d){
    d.x = c.x - b.x;
    d.y = c.y - b.y;
    return ccw(a,b,d);
}

long long dist(Point a, Point b)
{
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

bool ccw_cmp(Point a, Point b)
{
    long long c = ccw(points[0], a, b);

    if (c == 0)
        return dist(points[0], a) < dist(points[0], b);
    return c > 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t = 0;
    cin >> t;
    for (int tc = 0; tc < t; tc++)
    {
        int n;
        cin >> n;
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

        double total_dist = 0;
        for (int i = 0; i < nn; i++)
        {
            total_dist += dist(convex_points[i], convex_points[(i+1)%nn]);
        }

        double max_dist = 0;
        int a = 0;
        int b = 1;
        Point p1 = convex_points[0];
        Point p2 = convex_points[1];
        double cur_dist = dist(p1,p2);
        while (true){
            if (b <= a) break;

            if (min(cur_dist, max_dist-cur_dist) > cur_dist){
                p1 = convex_points[a];
                p2 = convex_points[b];
            }

            if (cur_dist > max_dist / 2. || b == n-1){
                a += 1;
                cur_dist -= dist(convex_points[a], convex_points[a-1]);
            }
            else{
                b += 1;
                cur_dist += dist(convex_points[b], convex_points[b-1]);
            }
        }

        cout << p1.x << ' ' << p1.y << ' ' << p2.x << ' ' << p2.y  << ' ' << dist(p1,p2) << '\n';
    }
}