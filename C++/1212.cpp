#include <bits/stdc++.h>

using namespace std;

string sa, sb;
int ma, reserva, carry, soma;

int main(){
	cin >> sa;
	cin >> sb;
	
	while (sa != "0" && sb != "0"){
		carry = 0;
		reserva = 0;
		
		ma = max(sa.size(), sb.size());
		
		
		sa = string(ma - sa.size(), '0') + sa;
		sb = string(ma - sb.size(), '0') + sb;
	
		
		for (int i = ma - 1; i >= 0; i--){
			soma = (sa[i] - '0') + (sb[i] - '0') + reserva;
			if (soma > 9) {
				reserva = 1;
				carry++;
			} else {
				reserva = 0;
			}
		}

		if (carry > 1){
			printf("%d carry operations.\n", carry);
		} else if (carry == 1) {
			printf("1 carry operation.\n");
		} else {
			printf("No carry operation.\n");
		}
		
		
		cin >> sa;
		cin >> sb;
	}
	return 0;
}
