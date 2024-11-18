#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void getNthLargest();
void swap();

int main(){
    int T;
    scanf("%d", &T);

    for (int i=0; i<T; i++){
        getNthLargest();
    }
}

void swap(int *x, int *y){
    int t = *x;
    *x = *y;
    *y = t;
}

void getNthLargest(){
    int A[10] = {0,};
    for (int i=0; i<10; i++){
        scanf("%d", &A[i]);
    }
    for (int i=0; i<9; i++){
        for (int j=0; j<9-i; j++){
            if (A[j] > A[j+1])
                swap(&A[j], &A[j+1]);
        }
    }
    printf("%d\n",A[7]);
}