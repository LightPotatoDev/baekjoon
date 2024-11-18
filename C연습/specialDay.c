#include <stdio.h>
#include <stdlib.h>

int main(){
    int m,d;
    scanf("%d",&m);
    scanf("%d",&d);
    if (m*30+d < 78){
        printf("Before");
    }
    else if (m*30+d == 78){
        printf("Special");
    }
    else{
        printf("After");
    }
}