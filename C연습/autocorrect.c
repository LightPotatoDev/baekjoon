#include <stdio.h>

int main(){
    char a;
    scanf("%c", &a);
    if (a == 'N' || a == 'n'){
        printf("Naver D2");
    }
    else{
        printf("Naver Whale");
    }
}