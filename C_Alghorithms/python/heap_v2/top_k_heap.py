# top k heap algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing

from heap_min import MinHeap


class TopKHeap:
    def __init__(self, k):
        """Initialize the TopKHeap data structure."""
        self.k = k
        self.sorted_elements = []
        self.min_heap = MinHeap()

    def size(self):
        """Return the total number of elements in the data structure."""
        return len(self.sorted_elements) + self.min_heap.size()

    def get_jth_element(self, j):
        """Retrieve the j-th element from the sorted elements array."""
        assert 0 <= j < self.k, "Index out of bounds"
        assert j < self.size(), "Index exceeds current size"
        return self.sorted_elements[j]

    def satisfies_assertions(self):
        """Check if the data structure satisfies its invariants."""
        for i in range(len(self.sorted_elements) - 1):
            assert self.sorted_elements[i] <= self.sorted_elements[i + 1], (
                f'Array is not sorted at position {i}, {self.sorted_elements[i]}, {self.sorted_elements[i + 1]}'
            )
        self.min_heap.satisfies_assertions()
        for i, element in enumerate(self.sorted_elements):
            assert element <= self.min_heap.min_element(), (
                f'Array element sorted_elements[{i}] = {element} is larger than min heap element {self.min_heap.min_element()}'
            )

    def insert_into_sorted(self, value):
        """Insert a value into the sorted elements list while maintaining order."""
        self.sorted_elements.append(value)
        index = len(self.sorted_elements) - 1
        while index > 0 and self.sorted_elements[index] < self.sorted_elements[index - 1]:
            self.sorted_elements[index], self.sorted_elements[index - 1] = (
                self.sorted_elements[index - 1],
                self.sorted_elements[index],
            )
            index -= 1

    def insert(self, value):
        """Insert a new element into the TopKHeap."""
        if self.size() < self.k:
            self.insert_into_sorted(value)
        else:
            self.insert_into_sorted(value)
            self.min_heap.insert(self.sorted_elements.pop())

    def delete_top_k(self, j):
        """Delete the j-th element from the sorted elements list."""
        assert 0 <= j < self.k, "Index out of bounds"
        assert self.size() > self.k, "Insufficient elements for deletion"
        self.sorted_elements.pop(j)
        self.sorted_elements.append(self.min_heap.min_element())
        self.min_heap.delete_min()


class TestTopKHeap:
    def run_tests(self):
        top_k_heap = TopKHeap(5)
        top_k_heap.sorted_elements = [-10, -9, -8, -4, 0]
        [top_k_heap.min_heap.insert(elt) for elt in [1, 4, 5, 6, 15, 22, 31, 7]]

        print('Initial data structure:')
        print('\t Sorted elements = ', top_k_heap.sorted_elements)
        print('\t MinHeap = ', top_k_heap.min_heap)

        # Test 1
        print('Test 1: Inserting element -2')
        top_k_heap.insert(-2)
        assert top_k_heap.sorted_elements == [-10, -9, -8, -4, -2], "Test 1 failed"
        assert top_k_heap.min_heap.min_element() == 0, "Test 1 failed"
        top_k_heap.satisfies_assertions()

        # Test 2
        print('Test 2: Inserting element -11')
        top_k_heap.insert(-11)
        assert top_k_heap.sorted_elements == [-11, -10, -9, -8, -4], "Test 2 failed"
        assert top_k_heap.min_heap.min_element() == -2, "Test 2 failed"
        top_k_heap.satisfies_assertions()

        # Test 3
        print('Test 3: delete_top_k(3)')
        top_k_heap.delete_top_k(3)
        assert top_k_heap.sorted_elements == [-11, -10, -9, -4, -2], "Test 3 failed"
        assert top_k_heap.min_heap.min_element() == 0, "Test 3 failed"
        top_k_heap.satisfies_assertions()

        # Test 4
        print('Test 4: delete_top_k(4)')
        top_k_heap.delete_top_k(4)
        assert top_k_heap.sorted_elements == [-11, -10, -9, -4, 0], "Test 4 failed"
        top_k_heap.satisfies_assertions()

        # Test 5
        print('Test 5: delete_top_k(0)')
        top_k_heap.delete_top_k(0)
        assert top_k_heap.sorted_elements == [-10, -9, -4, 0, 1], "Test 5 failed"
        top_k_heap.satisfies_assertions()

        # Test 6
        print('Test 6: delete_top_k(1)')
        top_k_heap.delete_top_k(1)
        assert top_k_heap.sorted_elements == [-10, -4, 0, 1, 4], "Test 6 failed"
        top_k_heap.satisfies_assertions()

        print('All tests passed.')


if __name__ == "__main__":
    tester = TestTopKHeap()
    tester.run_tests()
