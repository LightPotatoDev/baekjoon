#include <stdio.h>
#include <string.h>

int main(){
    int n;
    int pos1, pos2;
    char kbs1[] = "KBS1", kbs2[] = "KBS2";
    scanf("%d", &n);
    getchar();

    for (int i=0; i<n; i++){
        char buf[12];
        fgets(buf, 12, stdin);
        buf[strlen(buf)-1] = 0;
        if (strcmp(buf,kbs1) == 0)
            pos1 = i;
        if (strcmp(buf,kbs2) == 0)
            pos2 = i;
    }
    if (pos2 < pos1)
        pos2 += 1;

    for (int i=0; i<pos1; i++)
        printf("1");
    for (int i=0; i<pos1; i++)
        printf("4");
    for (int i=0; i<pos2; i++)
        printf("1");
    for (int i=0; i<pos2-1; i++)
        printf("4");

}