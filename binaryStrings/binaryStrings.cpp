/* Problem: given a binary string with wildcards, i.e. "1??0?101",
 * print all possible binary strings.
 */
#include <iostream>
#include <string>

using namespace std;
void getBinaryStrings(string binaryString, int startIndex) {
    // Look for wildcards
    for (int i = startIndex; i < binaryString.length(); i++) {
        // Recursive case: found wildcard. Recurse into replacing with both 0 and 1.
        if (binaryString[i] == '?') {
            string temp = binaryString;
            temp[i] = '0';
            getBinaryStrings(temp, i + 1);
            temp[i] = '1';
            getBinaryStrings(temp, i + 1);
            return;
        }
    }
    // Nonrecursive case: No wildcards, at end of recursion. Print string.
    cout << binaryString + "\n";
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cout << "Need a binary string!";
        return 1;
    }
    getBinaryStrings(argv[1], 0);
}