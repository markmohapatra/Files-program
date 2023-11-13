#include <stdio.h>

void printStr(char str[])
{
    int i=0;
    while (str[i]!='\0')
    {
        printf("%c", str[i]);
        i++;
    }
    printf("\n");
}
int main()
{
    // char str[] = {'m','a','r','k','\0'};
    // char str[5] = "mark";
     printf("Enter your string\n");
    char str[34];
    gets(str);
    printf("1.Using custom made function printStar:\n");
    printStr(str);

    printf("2.Using printf function:\n %s\n", str);

    printf("3.Using puts funtion: \n");
    puts(str);
    return 0;
}