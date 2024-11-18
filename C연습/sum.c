#include <stdio.h>
#include <stdlib.h>

int sum(int* arr){
    int i = 0;
    int s = 0;
    while (arr[i] >= 0){
        s += arr[i];
        i += 1;
    }
    return s;
}

int main(){
    int T;
    scanf("%d",&T);

    for (int tc=0; tc<T; tc++){
        int n;
        scanf("%d", &n);
        
        int *arr;
        arr = malloc(sizeof(int)*(n+1));
        for (int i=0; i<n; i++){
            scanf("%d", &arr[i]);
        }
        arr[n] = -1;
        printf("%d\n", sum(arr));
        free(arr);
    }
}