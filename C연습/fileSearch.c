#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void removeln(char *str){
    if (str[strlen(str)-1] == '\n')
        str[strlen(str)-1] = '\0';
}

int main(){
    char *str = calloc(2502, sizeof(char));
    fgets(str, 2502, stdin);

    char *search = calloc(52,sizeof(char));
    fgets(search, 52, stdin);

    removeln(str);
    removeln(search);

    int searched[2502] = {0,};
    int ans = 0;

    for (int i=0; str[i] != 0; i++){
        if (searched[i] == 1)
            continue;

        for (int j=0; search[j] != 0; j++){
            if (str[i+j] != search[j])
                break;
            
            if (search[j+1] == 0){
                ans += 1;
                for (int k=i; k < i+strlen(search); k++){
                    searched[k] = 1;
                }
            }
        }
    }

    printf("%d", ans);
}