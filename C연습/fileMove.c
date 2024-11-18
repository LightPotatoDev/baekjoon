#include <stdio.h>
#include <stdlib.h>

int min(int x, int y){
    if (x<y)
        return x;
    else
        return y;
}

int main(){
    int a,b,c,d;

    scanf("%d %d",&a,&b);
    scanf("%d %d",&c,&d);
    printf("%d",min(a+d, b+c));

    return 0;
}