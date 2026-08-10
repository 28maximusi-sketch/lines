// lines.cpp
#include <iostream>
#include <vector>
#include <random>
#include <string>
#include <iomanip>
#include <ctime>
#include <map>

using namespace std;

struct Puzzle {
    int size;
    vector<pair<pair<int,int>, pair<int,int>>> pairs;

    Puzzle(int sz, unsigned seed) : size(sz) {
        mt19937 rng(seed);
        if (size == 6) {
            pairs = {
                {{0,0},{5,5}}, {{0,1},{4,3}}, {{1,0},{3,4}},
                {{2,2},{4,4}}, {{3,1},{5,3}}, {{0,5},{5,0}}
            };
        } else {
            uniform_int_distribution<int> dist(0, size-1);
            for (int i = 0; i < size/2; ++i) {
                auto a = make_pair(dist(rng), dist(rng));
                auto b = make_pair(dist(rng), dist(rng));
                pairs.push_back({a,b});
            }
        }
    }

    void display(bool showSolution) const {
        string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        cout << "  ";
        for (int i = 0; i < size; ++i) cout << i+1 << " ";
        cout << endl;
        for (int r = 0; r < size; ++r) {
            cout << letters[r] << " ";
            for (int c = 0; c < size; ++c) {
                bool found = false;
                for (size_t idx = 0; idx < pairs.size(); ++idx) {
                    auto &p = pairs[idx];
                    if ((r == p.first.first && c == p.first.second) ||
                        (r == p.second.first && c == p.second.second)) {
                        cout << idx+1 << " ";
                        found = true;
                        break;
                    }
                }
                if (!found) cout << ". ";
            }
            cout << endl;
        }
    }
};

int main(int argc, char* argv[]) {
    int size = 6;
    bool showSolution = false;
    for (int i=1; i<argc; ++i) {
        string arg = argv[i];
        if (arg == "--size" && i+1 < argc) size = stoi(argv[++i]);
        else if (arg == "--show-solution") showSolution = true;
    }
    unsigned seed = time(nullptr);
    Puzzle p(size, seed);
    p.display(showSolution);
    return 0;
}
