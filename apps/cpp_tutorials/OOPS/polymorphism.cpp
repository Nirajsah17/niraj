#include<iostream>
using namespace std;


// functional overloading (Compile time)
class Math {
  public:
    int add(int a, int b){ return a + b;}
    float add(float a, float b){ return a + b;}
};


int main(){

  Math m;
  int a = m.add(2,3);
  cout << a <<endl;
  return 0;
}