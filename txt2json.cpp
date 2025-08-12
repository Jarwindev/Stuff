#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "Usage: " << argv[0] << " input.txt output.json\n";
        return 1;
    }

    ifstream fin(argv[1]);
    if (!fin) {
        cerr << "Error: Cannot open " << argv[1] << "\n";
        return 2;
    }

    ofstream fout(argv[2]);
    if (!fout) {
        cerr << "Error: Cannot open " << argv[2] << " for writing\n";
        return 3;
    }

    fout << "{\n";

    string word;
    bool first = true;
    while (getline(fin, word)) {
        if (word.empty()) continue; // skip empty lines
        if (!first) fout << ",\n";
        first = false;

        // Escape quotes if needed (shouldn't happen in plain wordlist)
        fout << "  \"" << word << "\": 1";
    }

    fout << "\n}\n";

    return 0;
}
