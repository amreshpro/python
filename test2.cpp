#include<iostream>

using namespace std;

class ABC{

private:
int a,b;
// constructor
public:
// constructor function / method
ABC(){
this->a = 0;
this->b = 0;
cout<<"I am in Constructor"<<endl;
}
// normal function / method
int sqr(){
    return this->a*this->a;
}
};


int main(){

// constructor call when object created - no need to call it automatically called by compiler
    ABC obj;

}