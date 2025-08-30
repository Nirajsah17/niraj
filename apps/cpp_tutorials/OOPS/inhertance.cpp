#include<iostream>
using namespace std;



class Animal {
  public:
    void speak(){
      cout << "Animal speaks" <<endl;
    }
  private:
    void type(){
      cout << "Which type of animals you are !!!" <<endl;
    }
};


class Dog : public Animal {
  public:
    void bark(){
      cout << "Dog barks" << endl;
    }
};


int main (){

  Dog d;

  d.speak();
  d.bark();
  return 0;
}