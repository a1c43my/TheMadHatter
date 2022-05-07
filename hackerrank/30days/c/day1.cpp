#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4,num;
    double d = 4.0,dub;
    string s = "HackerRank ",str,tmp; // this is how i define things :)
    
     getline(cin, tmp);
    num = stoi(tmp);

    getline(cin, tmp);
    dub = stod(tmp);
    // recommended method for getting the int and double  stoi() and stod()

    //standard getline     
    getline(cin, str);

    
    
    d += num;
    i += dub;
    cout<< i<<endl;
    
    cout<<fixed<<setprecision(1) <<d<<endl;
    
    cout<<s<<str<<endl;
    

    return 0;