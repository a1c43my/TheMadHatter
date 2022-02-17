#include<iostream>
#include<thread>

void DoSomething(){
	
	std::cout << "DoSomething()\n";
}

void DoSomething2() {
	std::cout << "DoSomething2S()\n";
}

int main(){
	std::thread thread_name(DoSomething); // name of function to call

	thread_name.join();

	std::cout<<"its done\n";
	std::thread thread_name2(DoSomething2); // name of function to call

	thread_name2.join();
}
