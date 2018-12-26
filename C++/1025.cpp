#include <bits/stdc++.h>

using namespace std;

int n, q, p, cont, o;
map<int, int> marbles;
map<int, int>::iterator it;

int main(){
	scanf("%d %d", &n, &q);
	while (n != 0 && q != 0){
		marbles.clear();
		
		for (int i = 0; i < n; i++){
			scanf("%d", &p);
			if (marbles.find(p) != marbles.end()){
				marbles[p] += 1;
			} else {
				marbles[p] = 1;
			}
		}

		printf("CASE# %d:\n", ++cont);
		for (int j = 0; j < q; j++){
			scanf("%d", &p);
			o = 0;
			if (marbles.find(p) != marbles.end()){
				
				for (it=marbles.begin(); it != marbles.find(p); it++){
					o += marbles[it->first];
				}
				o++;
				printf("%d found at %d\n", p, o);
			} else {
				printf("%d not found\n", p);
			}
		}
		scanf("%d %d", &n, &q);
	}
	return 0;
}
