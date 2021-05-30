#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, quebras = 0;
    cin >> n;

    for (int i = 0; i < n; i++){
        int l, c;
        cin >> l >> c;
        
        if (l > c) {
            quebras += c;
        }
    }

    cout << quebras << endl;
    return 0;
}
