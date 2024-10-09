#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class TwoWayMerger {
public:
    // Merges two sorted vectors into one sorted vector
    std::vector<int> merge_two_lists(const std::vector<int>& list1, const std::vector<int>& list2) {
        std::vector<int> merged_list;
        int i = 0, j = 0;

        // Merge until one list is exhausted
        while (i < list1.size() && j < list2.size()) {
            if (list1[i] < list2[j]) {
                merged_list.push_back(list1[i++]);
            }
            else {
                merged_list.push_back(list2[j++]);
            }
        }

        // Add remaining elements from either list
        while (i < list1.size()) {
            merged_list.push_back(list1[i++]);
        }

        while (j < list2.size()) {
            merged_list.push_back(list2[j++]);
        }

        return merged_list;
    }

    // Performs one step of merging in pairs for a list of sorted lists
    std::vector<std::vector<int>> one_step_k_way_merge(const std::vector<std::vector<int>>& list_of_lists) {
        if (list_of_lists.size() <= 1) {
            return list_of_lists;
        }

        std::vector<std::vector<int>> merged_lists;
        for (size_t i = 0; i < list_of_lists.size(); i += 2) {
            if (i + 1 < list_of_lists.size()) {
                merged_lists.push_back(merge_two_lists(list_of_lists[i], list_of_lists[i + 1]));
            }
            else {
                merged_lists.push_back(list_of_lists[i]);
            }
        }

        return merged_lists;
    }

    // Recursively merges a list of sorted lists into one sorted list
    std::vector<int> k_way_merge(std::vector<std::vector<int>> list_of_lists) {
        if (list_of_lists.size() == 1) {
            return list_of_lists[0];
        }

        std::vector<std::vector<int>> merged_lists = one_step_k_way_merge(list_of_lists);
        return k_way_merge(merged_lists);
    }
};

class TestMerger {
public:
    static void run_tests() {
        TwoWayMerger merger;

        // Test case 1
        std::vector<std::vector<int>> test_case1 = { {1, 2, 3}, {4, 5, 7}, {-2, 0, 6}, {5} };
        std::vector<int> result = merger.k_way_merge(test_case1);
        std::vector<int> expected1 = { -2, 0, 1, 2, 3, 4, 5, 5, 6, 7 };
        assert(result == expected1 && "Test Case 1 Failed");

        // Test case 2
        std::vector<std::vector<int>> test_case2 = { {-2, 4, 5, 8}, {0, 1, 2}, {-1, 3, 6, 7} };
        result = merger.k_way_merge(test_case2);
        std::vector<int> expected2 = { -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8 };
        assert(result == expected2 && "Test Case 2 Failed");

        // Test case 3
        std::vector<std::vector<int>> test_case3 = { {-1, 1, 2, 3, 4, 5} };
        result = merger.k_way_merge(test_case3);
        std::vector<int> expected3 = { -1, 1, 2, 3, 4, 5 };
        assert(result == expected3 && "Test Case 3 Failed");

        std::cout << "Two Way Merge Sort: All tests passed!\n";
    }
};
