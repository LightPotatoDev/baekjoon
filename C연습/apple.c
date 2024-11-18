#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int ans = 0;

    for (int i=0; i<n; i++){
        int a,b;
        scanf("%d %d", &a, &b);
        ans += b%a;
    }

    printf("%d",ans);
}