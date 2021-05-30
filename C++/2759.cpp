#include <iostream>

using namespace std;

int main() {
    char a, b, c;

    cin >> a >> b >> c;
    
    for (int i = 0; i < 3; i++) {
        cout << "A = " << a << ", B = " << b << ", C = " << c << endl;
        char tmp = a;
        a = b;
        b = c;
        c = tmp;
    }

    return 0;
}
