#include <iostream>

using namespace std;


void process(int* current, int* total, int value, int other) {
    if (*current == value) {
        *current = other;
        (*total)++;
    }
}

int main() {
    int n, ns[510], 
        c1 = 1, 
        t1 = 0, 
        c2 = 2, 
        t2 = 0,
        x;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;

        if (x == 1) {
            process(&c1, &t1, 2, 1);
            process(&c2, &t2, 2, 1);
        } else {
            process(&c1, &t1, 1, 2);
            process(&c2, &t2, 1, 2);
        }
    }
    
    if (t1 > t2) {
        cout << t1 << endl;
    } else {
        cout << t2 << endl;
    }

    return 0;
}
