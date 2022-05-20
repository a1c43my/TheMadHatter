#include <stdio.h>
#include <stdlib.h>

int main()
{
    char welcome[] = "\tHello world!\nThis will simulate how a hacker can use C to change a few things\n";
    char step1[] = "This is the directory you are in \n";
    char step2[] = "This is the secret file created when you ran this C program \n";


    system("whoami > c:\\users\\[user]\\Desktop\\hereiam2.txt");
    system("dir /B > c:\\users\\[user]\\Desktop\\hereiam.txt");
    printf(step1);
    system("pause");
    printf(step2);
    system("notepad.exe c:\\users\\[user]\\Desktop\\hereiam.txt");
    system("notepad.exe c:\\users\\[user]\\Desktop\\hereiam2.txt");
    printf(welcome);

    return 0;
}
