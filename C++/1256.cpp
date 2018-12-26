#include <bits/stdc++.h>

using namespace std;

int n, m, c, v;
map<int, vector<int> > mapa;
vector<int> lv;

int main(){
	scanf("%d", &n);
	for (int i = 0; i < n; i++){
		if (i != 0) {
			printf("\n");
		}
		mapa.clear();
		scanf("%d %d", &m, &c);
		for (int j = 0; j < c; j++){
			scanf("%d", &v);
			mapa[v % m].push_back(v);
		}
		for (int j = 0; j < m; j++){
			printf("%d", j);
			if (mapa.find(j) != mapa.end()){
				lv = mapa[j];

				for (int p = 0; p < lv.size(); p++){
					printf(" -> %d", lv[p]);
				}
			} 
			printf(" -> \\\n");
		}
	}
	return 0;
}

