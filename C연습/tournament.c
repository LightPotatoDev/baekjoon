#include <stdio.h>
#include <string.h>

int max(int x, int y){
    if (x > y) return x;
    else return y;
}

int main(){
    int n,a,b;
    scanf("%d %d %d", &n, &a, &b);

    int arr[100002];
    memset(arr, 0, sizeof(int)*100002);
    for (int i = 0; i<n; i++){
        if (i == a-1 || i == b-1)
            arr[i] = 2;
        else
            arr[i] = 1;
    }

    int ptr = 0;
    int round = 0;
    int flag = 0;
    while (1){
        round += 1;
        for (int i=0; arr[i] != 0; i+=2){
            int p1 = arr[i], p2 = arr[i+1];
            if (p1 == 2 && p2 == 2){
                flag = 1;
                break;
            }
            arr[i] = 0;
            arr[i+1] = 0;
            arr[i/2] = max(p1,p2);
        }
        if (flag == 1)
            break;
    }
    printf("%d", round);
}