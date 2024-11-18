#include <stdio.h>

int main(){
	int n, ans;
	scanf("%d",&n);
	
	for (int i=0; i<n; i++){
		int a;
		scanf("%d",&a);
		ans += a;
	}
	
	printf("%d\n", n);
	printf("%d", ans);
}
