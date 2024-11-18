#include <iostream>
#include <vector>
#include <complex>
#include <cmath>

using namespace std;

typedef complex<double> cd;
const double PI = acos(-1);

vector<cd> FFT(const vector<cd>& p, bool inv) {
    int n = p.size();
    if (n == 1) return p;
    
    vector<cd> pe(n / 2), po(n / 2);
    for (int i = 0; i < n / 2; ++i) {
        pe[i] = p[2 * i];
        po[i] = p[2 * i + 1];
    }
    
    vector<cd> ye = FFT(pe, inv);
    vector<cd> yo = FFT(po, inv);
    vector<cd> y(n);
    
    cd w = exp(cd(0, 2 * PI / n));
    if (inv) w = exp(cd(0, -2 * PI / n));
    
    cd wk(1, 0);
    for (int i = 0; i < n / 2; ++i) {
        y[i] = ye[i] + wk * yo[i];
        y[i + n / 2] = ye[i] - wk * yo[i];
        wk *= w;
    }
    
    return y;
}

vector<int> polyMul(vector<int>& A, vector<int>& B) {
    // Zero padding -> n = 2^m
    int n = 1;
    while (n < A.size() + B.size()) n <<= 1;
    
    A.resize(n);
    B.resize(n);
    
    vector<cd> ca(A.begin(), A.end()), cb(B.begin(), B.end());
    
    // Do polyMul using FFT
    vector<cd> va = FFT(ca, false);
    vector<cd> vb = FFT(cb, false);
    vector<cd> V(n);
    
    for (int i = 0; i < n; ++i) {
        V[i] = va[i] * vb[i];
    }
    
    vector<cd> res = FFT(V, true);

    vector<int> resInt(n);
    for (int i = 0; i < n; ++i) {
        res[i] /= cd(n, 0);
        resInt[i] = round(res[i].real());
    }
    
    return resInt;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(200001, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        A[x] = 1;
    }

    vector<int> B = polyMul(A, A);

    int ans = 0, m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (A[x] >= 1 || B[x] >= 1) {
            ans += 1;
        }
    }
    cout << ans;

    return 0;
}
