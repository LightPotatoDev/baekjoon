#include <stdio.h>
#include <stdlib.h>

int swap(int *x, int *y){
    int t = *x;
    *x = *y;
    *y = t;
}

int main(){
    int n;
    scanf("%d",&n);
    int cups[3] = {1,0,0};

    for (int i=0; i<n; i++){
        int a,b;
        scanf("%d %d", &a, &b);
        swap(&cups[a-1], &cups[b-1]);
    }

    for (int i=0; i<3; i++){
        if (cups[i] == 1){
            printf("%d", i+1);
        }
    }
}