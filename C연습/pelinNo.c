#include <stdio.h>
#include <string.h>

int main(){
    int n;
    scanf("%d",&n);
    getchar();

    char ch = 0;
    char target = 1;
    int flag = 1;
    int ind = 0;
    while ((ch = fgetc(stdin)) != EOF){
        if (ch != ' '){
            if (target == 1 && ind == 0)
                target = ch;
            if (target != 1 && ind == 0 && ch != target){
                flag = 0;
                break;
            }
            ind += 1;
        }
        if (ch == ' '){
            ind = 0;
        }
    }

    printf("%d", flag);
}