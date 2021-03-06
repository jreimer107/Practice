// Problem: find the number of permutations of strings of length n that contain
// at most 1 b and 2 c'ss. The rest of the letters are a's.
#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int maxLength = 0;
int maxB = 1;
int maxC = 2;
unordered_map <int, int> cache = {};

int getStrings(int stringLength, int numB, int numC) {
    // Non-recursive case, string at max length. Only this one possible, return 1.
    if (stringLength == maxLength) {
        return 1;
    }

    // Before recursing, check cache to see if we've done this before.
    int index = (stringLength << 3) + (numB << 2) + numC;
    unordered_map<int, int>::const_iterator iter = cache.find(index);
    if (iter != cache.end()) {
        return iter->second;
    }

    // Recursive case. If space, recurse into adding b and c. Always recurse into adding a.
    int stringsFound = 0;
    stringsFound += getStrings(++stringLength, numB, numC);
    if (numB < maxB) {
        stringsFound += getStrings(stringLength, numB + 1, numC);
    }
    if (numC < maxC) {
        stringsFound += getStrings(stringLength, numB, numC + 1);
    }
    cache.insert({index, stringsFound});
    return stringsFound;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cout << "Need a length!";
        return 1;
    }
    maxLength = atoi(argv[1]);
    cout << getStrings(0, 0, 0);
}