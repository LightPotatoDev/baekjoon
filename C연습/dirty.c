#include <stdio.h>

int main() {
    int array[] = {1, 3, 5, 7};
    int *pa = array;

    printf("Before: %d\n", *pa);  // Output: Before: 1
    printf("After: %d\n", ++*pa); // Output: After: 2
    
    return 0;
}
