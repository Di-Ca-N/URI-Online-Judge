#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;

    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string input;
        getline(cin, input);
        
        int sc0 = 0, ec0 = 0;
        bool c0s = false;
        int scs = 0, ecs = 0;
        bool css = false;

        int p = -1;

        for (char const &c: input){
            p++;
            bool output = false;

            if (c == '0') {
                if (c0s) {
                    ec0++;
                } else {
                    sc0 = p;
                    ec0 = p;
                    c0s = true;
                }
            } else {
                if (c0s) {
                    int comp_size = ec0 - sc0 + 1;
                    if (comp_size <= 2) {
                        for (int i = 0; i < comp_size; i++) {
                            cout << "0";
                        }
                    } else {
                        while (comp_size > 255) {
                            comp_size -= 255;
                            cout << "#" << (char) 255;
                        }
                        cout << "#" << (char) comp_size;
                    }
                    c0s = false;
                } else {
                    if (c == ' ') {
                        if (css) {
                            ecs++;
                        } else {
                            scs = p;
                            ecs = p;
                            css = true;
                        }
                    } else {
                        if (css) {
                            int comp_size = ecs - scs + 1;
                            if (comp_size <= 2) {
                                for (int i = 0; i < comp_size; i++) {
                                    cout << " ";
                                }
                            } else {
                                while (comp_size > 255) {
                                    comp_size -= 255;
                                    cout << "$" << (char) 255;
                                }
                                cout << "$" << (char) comp_size;
                            }
                            css = false;
                        }
                        cout << c;
                    }
                }
            }
        }
        cout << endl;
    }
    return 0;
}
