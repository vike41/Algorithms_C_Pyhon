#include <iostream>
#include "merge_sort.cpp"
#include "two_way_merge.cpp"
#include "heap_max.cpp"
#include "heap_min.cpp"

int main() {
    // Sort 
    printf("\n--------------------Sorting-------------------------\n");
    TestCrossoverFinder::run_tests();
    TestMerger::run_tests();
    
    // Heap 
    printf("\n--------------------Heap-------------------------\n");
    TestMaxHeap::run_tests();
    TestMinHeap::run_tests();

    return 0;
}
