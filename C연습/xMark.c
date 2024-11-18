#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){
    int n;
    scanf("%d",&n);
    getchar();

    char *ans;
    ans = malloc(n+1);

    for (int i=0; i<n; i++){
        char ch;
        int xSpot = 0;
        int mode = 0;
        int pt = 0;
        while ((ch=getchar()) != '\n'){
            if (mode == 0){
                if (ch == 'x' || ch == 'X')
                    xSpot = pt;
                pt += 1;
            }
            if (mode == 1){
                if (pt == xSpot)
                    ans[i] = toupper(ch);
                pt += 1;
            }
            if (ch == ' '){
                pt = 0;
                mode = 1;
            }
        }
    }
    ans[n] = 0;
    fputs(ans, stdout);

}