#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int yCost = 0;
    int mCost = 0;

    for (int i=0; i<n; i++){
        int time;
        scanf("%d", &time);
        yCost += (time+30)/30*10;
        mCost += (time+60)/60*15;
    }

    if (yCost < mCost){
        printf("Y %d", yCost);
    }
    else if (yCost > mCost){
        printf("M %d", mCost);
    }
    else{
        printf("Y M %d", yCost);
    }
}