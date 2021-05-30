#include <bits/stdc++.h>

using namespace std;

int main () {
    int x;
    cin >> x;
    string c;

    if (x == 0) c = "E";    
    else if (x <= 35) c = "D";
    else if (x <= 60) c = "C";
    else if (x <= 85) c = "B";
    else c = "A";

    cout << c << endl;
    return 0;
}
