#include <bits/stdc++.h>

#define MAXN 10001
#define MAXC 201

using namespace std;

char listaTelefonica[MAXN][MAXC];
int n, econ;


int main(){
	while (scanf("%d", &n) != EOF){
		for (int i = 0; i < n; i++){
			scanf("%s", listaTelefonica[i]);
		}	
		
		sort(*listaTelefonica, *listaTelefonica+n);

		for (int i = 0; i < n; i++){
			printf("%s\n", listaTelefonica[i]);
		}

	}

}