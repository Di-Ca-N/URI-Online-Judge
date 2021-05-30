#include <bits/stdc++.h>

using namespace std;

int main() {
    int d, x, y, z;
    cin >> d >> x >> y >> z;
    int m = min<int>({d, x, y, z});

    if (m < d) {
        cout << "N" << endl;
    } else {
        cout << "S" << endl;
    }
    return 0;
}
