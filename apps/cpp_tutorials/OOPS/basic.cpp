#include<iostream>
#include<string>
using namespace std;


class Person {
  public:
    string name;
    int age;

    void greet(){
      cout << "Hii, I'm " << name << endl;
    }
};



int main (){
  Person P;
  P.name = "Niraj";
  P.age = 25;
  P.greet();
  return 0;
}