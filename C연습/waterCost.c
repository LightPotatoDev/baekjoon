#include <stdio.h>
#include <stdlib.h>

int main(){
    int a,b,c,d,p;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    scanf("%d",&d);
    scanf("%d",&p);

    int cost1 = a*p;
    int cost2 = 0;
    if (p <= c)
        cost2 = b;
    else
        cost2 = b + (p-c)*d;

    if (cost1 < cost2)
        printf("%d",cost1);
    else
        printf("%d", cost2);
}