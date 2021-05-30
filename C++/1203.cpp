#include <bits/stdc++.h>

using namespace std;

int restante[110][5000] = {{0}};
int pontes[110] = {0};
int r, k;

int knapsack(int obj, int espaco_livre) {
    if (restante[obj][espaco_livre] != 0) return restante[obj][espaco_livre];
    if (espaco_livre == 0 || obj >= r) return restante[obj][espaco_livre] = 0;
    int nao_conta = knapsack(obj + 1, espaco_livre);
    if (pontes[obj] <= espaco_livre) {
        int conta = 1 + knapsack(obj + 1, espaco_livre - pontes[obj]);
        return restante[obj][espaco_livre] = max(conta, nao_conta);
    }
    return restante[obj][espaco_livre] = nao_conta;
}

int main() {
    ios::sync_with_stdio(false);

    while (!cin.eof()) {
        cin >> r >> k;

        int a, b;

        for (int i = 0; i < k; i++) {
            cin >> a >> b;
            pontes[a - 1]++;
            pontes[b - 1]++;
        }
        int m = knapsack(0, k);
        if (m == k) {
            cout << "S" << endl;
        } else {
            cout << "N" << endl;
        }
    }
    return 0;
}