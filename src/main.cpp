#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K;
    cin >> K;

    unordered_map<char,int> val;
    for (int i = 0; i < K; i++) {
        char c;
        int v;
        cin >> c >> v;
        val[c] = v;
    }

    string A, B;
    cin >> A >> B;

    int n = A.size(), m = B.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (A[i-1] == B[j-1]) {
                dp[i][j] = dp[i-1][j-1] + val[A[i-1]];
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    string res = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (A[i-1] == B[j-1]) {
            res.push_back(A[i-1]);
            i--;
            j--;
        } else if (dp[i-1][j] >= dp[i][j-1]) {
            i--;
        } else {
            j--;
        }
    }

    reverse(res.begin(), res.end());

    cout << dp[n][m] << "\n";
    cout << res << "\n";

    return 0;
}
