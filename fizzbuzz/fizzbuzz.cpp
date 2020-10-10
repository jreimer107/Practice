#include <iostream>
#include <string>

using namespace std;
int main(int argc, char *argv[]) {
    if (argc != 2) {
        cout << "Must enter a number!";
    } else {
        for (int i = 1; i <= atoi(argv[1]); i++) {
            string msg = "";
            bool divisBy3 = i % 3 == 0;
            bool divisBy5 = i % 5 == 0;
            if (divisBy3 && divisBy5) {
                msg += "Fizz buzz";
            } else if (divisBy3) {
                msg += "Fizz";
            } else if (divisBy5) {
                msg += "Buzz";
            } else {
                msg += to_string(i);
            }
            cout << msg + "\n";
        }
    }
    return 0;
}