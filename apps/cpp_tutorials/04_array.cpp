#include <iostream>
#include <string>
using namespace std;


int main(){

  int arr[3] = {1, 2, 3};
  cout << arr <<endl;
  cout << arr[1] << endl;

  for(int i = 0; i < 3 ; i++){
    cout << arr[i] << " ,";
  }
  cout << endl;

  return 0;
}