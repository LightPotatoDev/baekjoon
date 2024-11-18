#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct car{
    int passengers;
    int letters[26];
} CAR;

void chooseCar(CAR *tr, char c, int n, int k){
    int *candidate;
    candidate = calloc(n,sizeof(int));

    int letterNum = 100;
    for (int i=0; i<n; i++){
        if (tr[i].passengers >= k)
            continue;
        if (tr[i].letters[c-'a'] <= letterNum){
            if (tr[i].letters[c-'a'] < letterNum)
                memset(candidate,0,n*sizeof(int));
            candidate[i] = 1;
            letterNum = tr[i].letters[c-'a'];
        }
    }

    int passNum = 100;
    for (int i=0; i<n; i++){
        if (tr[i].passengers >= k)
            continue;
        if (tr[i].passengers <= passNum && candidate[i] == 1){
            if (tr[i].passengers < passNum)
                memset(candidate,0,i*sizeof(int));
            passNum = tr[i].passengers;
        }
    }

    int carNum = 0;
    for (int i=0; i<n; i++){
        if (candidate[i] == 1){
            carNum = i;
            break;
        }
    }

    tr[carNum].passengers += 1;
    tr[carNum].letters[c-'a'] += 1;

    /*for (int i=0; i<n; i++){
        printf("%d ", candidate[i]);
    }
    printf("\n");*/
}

int main(){
    int n,k,p;
    scanf("%d %d",&n,&k);
    scanf("%d", &p);
    getchar();

    CAR train[n];

    for (int i=0; i<n; i++){
        train[i].passengers = 0;
        memset(train[i].letters,0,26 * sizeof(int));
    }

    for (int i=0; i<p; i++){
        char name[12];
        fgets(name,sizeof(name),stdin);
        chooseCar(train,name[0],n,k);
        /*for (int j=0; j<n; j++){
            printf("%d ",train[j].passengers);
        }
        printf("\n");*/
    }

    for (int i=0; i<n; i++){
        printf("%d ",train[i].passengers);
    }
}