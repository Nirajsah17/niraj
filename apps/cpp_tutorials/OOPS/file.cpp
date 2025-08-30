
#include<iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream file("example.txt"); // Create or overwrite

    if (file.is_open()) {
        file << "Hello, Niraj!\n";
        file << "This is written to a file.";
        file.close();
    } else {
        cout << "Unable to open file.";
    }

    return 0;
}
