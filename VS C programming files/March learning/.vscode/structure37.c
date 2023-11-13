#include <stdio.h>
#include <string.h>
struct Student
{
    int id;
    int marks;
    char fav_char;
    char name[34];
}mark, harry, ravi;

//global variable
//struct Student mark, harry, ravi;
void print()
    {
        printf("%s", mark.name);
    }

int main()
{
    //private variable
    //struct Student mark, harry, ravi;
    mark.id = 1;
    harry.id = 2;
    ravi.id = 3;
    mark.marks = 466;    
    harry.marks = 46;
    ravi.marks = 43;

    mark.fav_char  ='p';    
    harry.fav_char = 'y';
    ravi.fav_char  ='t';

    strcpy(mark.name, " Mark student of the year");
    // printf("Mark got %d marks\n", mark.marks);
    // printf("Mark's name is: %s\n", mark.name);
    print();
    return 0;
}