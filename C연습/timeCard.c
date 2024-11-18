#include <stdio.h>
#include <stdlib.h>

int main(){
    for (int i=0; i<3; i++){
        int hi, mi, si, hf, mf, sf;
        scanf("%d %d %d %d %d %d",&hi, &mi, &si, &hf, &mf, &sf);
        int workSec = hf*3600+mf*60+sf-(hi*3600+mi*60+si);
        int h,m,s;

        h = workSec / 3600;
        workSec %= 3600;
        m = workSec / 60;
        workSec %= 60;
        s = workSec;

        printf("%d %d %d\n",h,m,s);
    }
}