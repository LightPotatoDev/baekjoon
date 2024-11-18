#include <stdio.h>
#include <stdlib.h>

void convertBinary(int n){
    int *arr;
    arr = malloc(sizeof(int));
    int len = 0;

    while (n>1){
        arr[len] = n%2;
        n /= 2;
        arr = realloc(arr, sizeof(int)*(len+2));
        len += 1;
    }
    arr[len] = 1;
    len += 1;

    for(int i = 0; i < len; i++){
        if (arr[i] == 1)
            printf("%d ", i);
    }
    printf("\n");
}

int main(){
    int T;
    scanf("%d",&T);

    for (int tc=0; tc<T; tc++){
        int n;
        scanf("%d", &n);
        convertBinary(n);
    }
}