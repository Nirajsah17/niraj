#include <iostream>
#include <string>
using namespace std;


int main (){

  string name;
  int age;
  float height;
  char grade;

  cout << "Enter your name :" << endl;
  cin >> name;

  cout << "Enter your Height :" << endl;
  cin >> height;
  cout << "Enter your Age :" << endl;
  cin >> age;
  cout << "Enter your grade :" << endl;
  cin >> grade;


  cout << "----------------------------- "<< endl;
  cout << " Name : " << name << endl;
  cout << " Age : " << age << endl;
  cout << " Height : " << height << endl;
  cout << " Grade : " << grade << endl;
  cout << "----------------------------- "<< endl;
  return 0;
}