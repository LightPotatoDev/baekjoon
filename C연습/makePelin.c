#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void removeln(char *str){
    if (str[strlen(str)-1] == '\n')
        str[strlen(str)-1] = '\0';
}

int main(){
    char *str = calloc(52,1);
    fgets(str, 52, stdin);
    removeln(str);

    int len = strlen(str);
    int ans = len;

    for (ans = len; ans < len*2-1; ans++){
        int flag = 1;

        for (int i = ans/2; str[i] != 0; i++){
            
            if (str[i] != str[ans-i-1]){
                flag = 0;
                break;
            }
        }

        if (flag == 1){
            break;
        }
    }

    printf("%d",ans);
}