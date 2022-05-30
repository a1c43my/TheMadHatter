#include <stdio.h>
#include <stdlib.h>


int main()
{
    char msg[] = "Welcome, make a selection\n";
    char options[] = "\t[0] Config \n\t[1] Add User\n\t[2] Login\n\t[E] Exit\n\t[M] System Mode\n";
    char in1[1];
    printf("%s",msg); // %c is incorrect here, use %s
    printf("%s",options);

// begin switching based on input
int counter = 0;
while (counter < 1) {

    scanf("%s",in1);
    printf("Selection Made !!!\n\n");
    switch(in1[0]) {
    char file1[1];
    char file2[1];
    case '0':

      system("cls");
      printf("Checking for config file\n");
      system("powershell -c Test-Path ./config.txt && powershell -c Test-Path ./config.log");
      printf("\nEnter 0 or 1 to indicate config file presence\n");
      printf("File 1: ");
      scanf("%s",file1);
        if(file1[0] == '0'){
        printf("\nfile 1 missing\n\n");
        }
        else if(file1[0] == '1'){
            printf("\nfile 1 present\n\n");
        }
        else{
            printf("\nFILE ERROR 006 - file1\n");
        }
      printf("File 2: ");
      scanf("%s",file2);
       if(file2[0] == '0'){
        printf("\nfile 2 missing\n");
        }
        else if(file2[0] == '1'){
            printf("\nfile 2 present\n\n");
        }
        else{
            printf("\nFILE ERROR 006 - file2\n");
        }
      break;
    case '1':
      system("cls");
      printf("User Database\n");
      break;
    case '2':
      system("cls");
      printf("Login Sequence\n");
      break;
    case 'M':
      system("cls");
      printf("System Mode\n\nconfig file:");
      break;
    case 'E':
      printf("Exiting !!! \n");
      system("cls");
      break;

    default:
      system("cls");
      printf("Unknown entry SYSTEM ERR 002\n");
      break;
  }

    counter++;
  }

    return 0;
}
