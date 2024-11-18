#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

struct Point{
    long long x,y;
    bool operator < (const Point &a){
        if (y == a.y)
            return x < a.x;
        return y < a.y;
    }
};
vector<Point> points;

long long ccw(const Point &a, const Point &b, const Point &c){
    return a.x * b.y + b.x * c.y + c.x *a.y - a.y * b.x - b.y * c.x - c.y * a.x;
}

long long dist(const Point &a, const Point &b){
    return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y);
}

bool ccw_cmp(const Point &a, const Point &b){
    long long c = ccw(points[0],a,b);

    if (c == 0)
        return dist(points[0],a) < dist(points[0],b);
    return c > 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    points.resize(n);
    for (int i=0; i<n; i++){
        long long x,y;
        cin >> x >> y;
        points[i].x = x;
        points[i].y = y;
    }

    sort(points.begin(), points.end());
    sort(points.begin()+1, points.end(), ccw_cmp);
    stack<Point> stk;
    stk.push(points[0]);
    stk.push(points[1]);

    for (int i=2; i<n; i++){
        while (stk.size() >= 2){
            Point p1 = stk.top();
            stk.pop();
            Point p2 = stk.top();
            if (ccw(p2, p1, points[i]) > 0){
                stk.push(p1);
                break;
            }
        }
        stk.push(points[i]);
    }

    cout << stk.size();
}