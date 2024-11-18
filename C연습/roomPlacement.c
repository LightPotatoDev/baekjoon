#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int n,k;
    scanf("%d %d", &n, &k);

    int stud[12] = {0,};

    for (int i=0; i<n; i++){
        int s,y;
        scanf("%d %d", &s, &y);
        stud[s*6+y-1] += 1;
    }

    int ans = 0;
    for (int i=0; i<12; i++){
        ans += ceil((float)stud[i]/k);
    }
    printf("%d", ans);
}