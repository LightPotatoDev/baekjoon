#include <stdio.h>
#include <stdlib.h>

int main(){
    long long int a,b;
    scanf("%lld %lld",&a,&b);
    if (a>b){
        long long int t = a;
        a = b;
        b = t;
    }
    long long int ans = -1*(a-b-1)*(a+b)/2;
    printf("%lld",ans);
}