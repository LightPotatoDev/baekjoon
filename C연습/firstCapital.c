#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void capitalize(char *str){
    
    str[0] = toupper(str[0]);
    fputs(str, stdout);
}

int main(){
    int n;
    scanf("%d", &n);
    getchar();

    for (int i=0; i<n; i++){
        char *buf = malloc(40);
        memset(buf,0,40);
        fgets(buf, 40, stdin);
        capitalize(buf);
        free(buf);
    }
}