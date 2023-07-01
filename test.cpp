#include<iostream>

using namespace std;

int fun(int a){
    return a*a;
}

int fun(int a,int b){
    return a * b;
}

int main(){


int res1 = fun(5);
int res2 = fun(2,8);
cout<<res1<<endl;
cout<<res2<<endl;





    return 0;
}