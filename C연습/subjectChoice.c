#include <stdio.h>
#include <stdlib.h>

int main(){
    int sum = 0, low1 = 100, low2 = 100;
    for (int i=0; i<6; i++){
        int score = 0;
        scanf("%d", &score);
        if (i < 4 && score < low1)
            low1 = score;
        if (i >= 4 && score < low2)
            low2 = score;
        
        sum += score;
    }
    printf("%d",sum-low1-low2);
    return 0;
}