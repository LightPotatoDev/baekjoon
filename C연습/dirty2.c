#include <stdio.h>

int main() {
    int array[] = {1, 3, 5, 7};
    int *pa = array;

    printf("Current: %d\n", *pa); // Output: Current: 1
    printf("Next: %d\n", *pa++);  // Output: Next: 1

    printf("New Current: %d\n", *pa); // Output: New Current: 2
    
    return 0;
}
