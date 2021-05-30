#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, estrelas[1000010], atacadas[1000010] = {0};
    long long int total = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> estrelas[i];
        total += estrelas[i];
    }

    int current = 0;

    while (current >= 0 and current < n) {
        atacadas[current] = 1;
        int carneiros = estrelas[current];

        if (carneiros > 0) {
            estrelas[current]--;
            total--;
        }

        if (carneiros % 2 == 1) current++;
        else current--;
    }

    int total_atacadas = 0;

    for (int i = 0; i < n; i++) {
        total_atacadas += atacadas[i];
    }

    cout << total_atacadas << " " << total << endl;
    return 0;
}
