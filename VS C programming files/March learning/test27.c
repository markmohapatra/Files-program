#include <stdio.h>
int main()
{
    int a = 34;
    int* ptra = &a; 
    printf("The address of a by pointer %d\n", ptra);
    printf("The address plus one is %d\n", ptra+1);

    return 0;
}