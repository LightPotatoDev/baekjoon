#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_LEN 200000

void removeln(char *str){
    if (str[strlen(str)-1] == '\n')
        str[strlen(str)-1] = '\0';
}

int contains(char *str, char *substr){
    int i=0, j=0;
    for (i=0; str[i] != 0; i++){
        if (str[i] != substr[j]){
            j = 0;
        }
        if (str[i] == substr[j]){
            j += 1;
            if (substr[j] == 0)
                return 1;
        }
    }
    return 0;
}
    
    

int main(){
    char *a, *b, *ans;
    a = malloc(MAX_LEN+2);
    b = malloc(MAX_LEN+2);
    ans = malloc(MAX_LEN+2);

    fgets(a, MAX_LEN+2, stdin);
    fgets(b, MAX_LEN+2, stdin);
    fgets(ans, MAX_LEN+2, stdin);

    removeln(a);
    removeln(b);
    removeln(ans);

    int c1 = contains(a, ans);
    int c2 = contains(b, ans);

    if (c1 == 1 && c2 == 1)
        printf("YES");
    else
        printf("NO");

    free(a);
    free(b);
    free(ans);
}