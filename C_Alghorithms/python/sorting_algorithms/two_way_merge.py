# Two way sort algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing

class TwoWayMerger(object):
    def merge_two_lists(self, list1, list2):
        """Merges two sorted lists into one sorted list."""
        merged_list = []
        i, j = 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1

        # Add remaining elements from either list
        merged_list.extend(list1[i:])
        merged_list.extend(list2[j:])

        return merged_list

    def one_step_k_way_merge(self, list_of_lists):
        """Performs one step of merging in pairs for a list of sorted lists."""
        if len(list_of_lists) <= 1:
            return list_of_lists

        merged_lists = []
        for i in range(0, len(list_of_lists), 2):
            if i + 1 < len(list_of_lists):
                merged_lists.append(self.merge_two_lists(list_of_lists[i], list_of_lists[i + 1]))
            else:
                merged_lists.append(list_of_lists[i])

        return merged_lists

    def k_way_merge(self, list_of_lists):
        """Recursively merges a list of sorted lists into one sorted list."""
        if len(list_of_lists) == 1:
            return list_of_lists[0]

        merged_lists = self.one_step_k_way_merge(list_of_lists)
        return self.k_way_merge(merged_lists)


class TestMerger:

    @staticmethod
    def run_tests():
        merger = TwoWayMerger()

        # Test case 1
        result = merger.k_way_merge([[1, 2, 3], [4, 5, 7], [-2, 0, 6], [5]])
        assert result == [-2, 0, 1, 2, 3, 4, 5, 5, 6, 7], "Test Case 1 Failed"

        # Test case 2
        result = merger.k_way_merge([[-2, 4, 5, 8], [0, 1, 2], [-1, 3, 6, 7]])
        assert result == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], "Test Case 2 Failed"

        # Test case 3
        result = merger.k_way_merge([[-1, 1, 2, 3, 4, 5]])
        assert result == [-1, 1, 2, 3, 4, 5], "Test Case 3 Failed"

        print('Two way merge: All tests passed!')


if __name__ == "__main__":
    TestMerger.run_tests()
