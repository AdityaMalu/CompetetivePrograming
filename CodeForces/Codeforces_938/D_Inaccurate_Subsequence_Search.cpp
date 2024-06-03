// Link : https://codeforces.com/contest/1955/problem/D

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        
        vector<int> a(n);
        vector<int> b(m);
        
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        
        for (int i = 0; i < m; ++i) {
            cin >> b[i];
        }
        
        unordered_map<int, int> dicta;
        unordered_map<int, int> dictb;
        
        for (int i : b) {
            dictb[i]++;
        }
        
        for (int i = 0; i < m; ++i) {
            dicta[a[i]]++;
        }
        
        int ans = 0;
        int c = 0;
        
        for (const auto& kv : dictb) {
            c += min(dicta[kv.first], kv.second);
        }
        
        if (c >= k) {
            ans++;
        }
        
        for (int i = m; i < n; ++i) {
            dicta[a[i - m]]--;
            if (dictb[a[i - m]] > dicta[a[i - m]]) {
                c--;
            }
            dicta[a[i]]++;
            if (dictb[a[i]] >= dicta[a[i]]) {
                c++;
            }
            if (c >= k) {
                ans++;
            }
        }
        
        cout << ans << endl;
    }
    
    return 0;
}
