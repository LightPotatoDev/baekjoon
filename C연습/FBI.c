#include <stdio.h>
#include <stdlib.h>

int main(){
    int noFBI = 1;
    for (int i=0; i<5; i++){
        char *str = malloc(13);
        fgets(str,12,stdin);

        for (int j=0; j<8; j++){
            if (str[j] == 'F' && str[j+1] == 'B' && str[j+2] == 'I'){
                printf("%d ",i+1);
                noFBI = 0;
                break;
            }
        }
        free(str);
    }

    if (noFBI)
        printf("HE GOT AWAY!");
}