#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void shift(char *str){
    
    for (int i=0; str[i] != 0; i++){
        if (str[i] == 'Z')
            str[i] -= 25;
        else if (str[i] != '\n')
            str[i] += 1;
    }
    fputs(str, stdout);
}

int main(){
    int n;
    scanf("%d", &n);
    getchar();

    for (int i=0; i<n; i++){
        char *buf = malloc(60);
        memset(buf,0,60);
        fgets(buf, 60, stdin);
        printf("String #%d\n", i+1);
        shift(buf);
        free(buf);
        printf("\n");
    }
}