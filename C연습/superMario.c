#include <stdio.h>
#include <stdlib.h>

int main(){
    int A[11] = {0,};
    for (int i=1; i<=10; i++){
        scanf("%d", &A[i]);
        A[i] += A[i-1];
    }
    
    int ans = 0;
    for (int i=0; i<11; i++){
        int score = A[i];
        if (abs(score-100) < abs(ans-100)){
            ans = score;
        }
        if (abs(score-100) == abs(ans-100) && ans < score){
            ans = score;
        }
    }

    printf("%d", ans);
}