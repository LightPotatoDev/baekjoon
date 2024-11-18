#include <stdio.h>

int main(){
    char ch;
    ch = getchar();

    switch (ch)
    {
    case 'M': printf("MatKor"); break;
    case 'W': printf("WiCys"); break;
    case 'C': printf("CyKor"); break;
    case 'A': printf("AlKor"); break;
    case '$': printf("$clear"); break;
    }
}