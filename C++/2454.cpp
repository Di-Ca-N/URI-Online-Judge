#include <iostream>

using namespace std;

int main() {
    int p, r;

    cin >> p >> r;
    char out;
    if (p == 0) {
        out = 'C';
    } else if (r == 0) {
        out = 'B';
    } else {
        out = 'A';
    }

    cout << out << endl;
    return 0;
}
