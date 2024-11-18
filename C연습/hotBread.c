#include <stdio.h>
#include <stdlib.h>

int main(){
    int n,m;
    scanf("%d %d\n",&n, &m);
    //getchar();

    for (int i=0; i<n; i++){
        char *str = malloc(m+1);
        gets(str);

        for (int j=0; j<m; j++){
            printf("%c",str[m-j-1]);
        }
        printf("\n");
        free(str);
    }
}