#include<iostream>
#include<stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

int main(int argc, char **argv){
//vars and things 
int port;
 //set port #


    if(argc < 2){
        std::cout<<"Defualt port 4545 set"<<std::endl;
        port = 4545; // default if no argument
    }
    else {
            port = atio(argv[1]); // accept port # 

            // socket and binding 
            int sock = socket(AF_INET, SOCK_STREAM, 0);
            //holds the socket info 
            struct sockaddr_in address;
            address.sin_family = AF_INET;
            address.sin_port = htons(port);
            //bind 
            int bind_value = bind(sock, (struct sockaddr*)&address, sizeof(address));

            if (bind_value < 0) {
                perror("some error here");
                return 1;
            }

            // accept connection
    }
}
