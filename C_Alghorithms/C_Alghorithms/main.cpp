#include <iostream>
#include "merge_sort.cpp"
#include "two_way_merge.cpp"

int main() {

    TestCrossoverFinder::run_tests();
    TestMerger::run_tests();

    return 0;
}
