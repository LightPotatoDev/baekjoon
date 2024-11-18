#include <stdio.h>
#include <stdlib.h>

typedef struct position{
    int x;
    int y;
} POS;

int main(int argc, char *argv[]){
    if (argc < 2) exit(0);

    FILE *input = NULL, *output = NULL;
    input = fopen(argv[1], "r");
    output = fopen("xorOutput.txt", "w");

    char digits[10];
    fgets(digits, 10, input);
    int n = atoi(digits);
    POS *pos = malloc(sizeof(int)*2);
    fgetc(input); // delete \n

    int i=0, j=0, cnt=0;
    char ch = 0;

    while ((ch = fgetc(input)) != EOF){
        if (ch == '1'){
            pos[cnt].x = j+1;
            pos[cnt].y = i+1;
            pos = realloc(pos, (sizeof(int) * 2) * (cnt+2));
            cnt += 1;
        }
        if (ch == ' ')
            j += 1;
        if (ch == '\n'){
            j = 0;
            i += 1;
        }
    }

    fprintf(output, "%d\n", cnt);
    for (i=0; i<cnt; i++){
        fprintf(output, "%d %d %d %d\n", pos[i].x, pos[i].x, pos[i].y, pos[i].y);
    }
}