#include <stdio.h>
#include <string.h>
int main()
{
    char s1[] = "mark";
    char s2[] = "raavi";
    char s3[54];
    printf("The strcmp for s1, s2 returned %d\n", strcmp(s1,s2));
    //puts(strcat(s1,s2)); 
    printf("The the length of s1 is %d\n", strlen(s1));
    printf("The the length of s2 is %d\n", strlen(s2));
    printf("The the reverse string s1 is: ");
     puts(strrev(s1));
     printf("The the reverse string s2 is: ");
     puts(strrev(s2));

     strcpy(s3, strcat(s1,s2));
     puts(s3);
     
    return 0;
}