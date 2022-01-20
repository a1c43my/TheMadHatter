#pragma once
#include<iostream>
#include<string>
// trying out a define method for output
#define out(x) std::cout << x << std::endl;
#define outn(x) std::cout << x;
#define outty std::cout <<

std::string msg = "hello and welcome to your first programming language! Remember me? Good ol CPP?";


void gameBoard_empty() {
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
}

void gameBoard_x_center() {
	out("\t |\t |\t ");
	out("\t |   x   |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
}
void gameBoard_x_topleft() {
	out("\t |\t |\t ");
	out("    x    |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
}

void gameBoard_o_center() {
	out("\t |\t |\t ");
	out("\t |   o   |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
}

void gameBoard_o_topleft() {
	out("    o    |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("_ _ _ _ _ _ _ _ _ _ _ _ _ _");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
	out("\t |\t |\t ");
}




