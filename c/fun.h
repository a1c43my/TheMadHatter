#include<iostream>
#include<fstream>
#include<string>
using namespace std;

void readFile_Named(string filename) {
	string text_read;
	fstream readFile(filename);
	if (readFile.is_open()){
		cout << "file opened \n";
		getline(cin, text_read);
		cout << text_read << "\n";
		while (readFile.peek() != EOF) {
			getline(cin, text_read);
			cout << text_read << "\n";
		}
	}

	if (!readFile.is_open()) { cout << "file might not exist \n"; }
	
	readFile.close();
}
