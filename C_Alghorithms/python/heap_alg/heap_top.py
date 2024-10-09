# Two way sort algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing
from heap_min import MinHeap


class TopKHeap:
    """A data structure to maintain the top K elements using a sorted list (A) and a min-heap (H)."""

    def __init__(self, k):
        """Initialize the TopKHeap with an empty sorted list (A) and a min-heap (H)."""
        self.k = k
        self.sorted_list = []  # Sorted list to hold the top K elements
        self.heap = MinHeap()  # Min-heap to hold the rest of the elements

    def size(self):
        return len(self.sorted_list) + self.heap.size()

    def get_element_at(self, j):
        if 0 <= j < self.k:
            print("Index out of bounds.")
        if j < self.size():
            print("Index exceeds size of the data structure.")
        return self.sorted_list[j]

    def validate_data_structure(self):
        self._validate_sorted_list()
        self.heap.satisfies_assertions()
        self._validate_sorted_list_vs_heap()

    def _validate_sorted_list(self):
        """Ensure that the sorted list (A) is sorted."""
        for i in range(len(self.sorted_list) - 1):
            assert self.sorted_list[i] <= self.sorted_list[i + 1], \
                f"Array A is not sorted at position {i}: {self.sorted_list[i]} > {self.sorted_list[i + 1]}"

    def _validate_sorted_list_vs_heap(self):
        """Ensure that every element in sorted list (A) is less than or equal to the elements in the heap."""
        for i, value in enumerate(self.sorted_list):
            assert value <= self.heap.min_element(), \
                f"Element A[{i}] = {value} is larger than heap min element {self.heap.min_element()}"

    def insert_into_sorted_list(self, elt):
        """Insert an element into the sorted list (A), maintaining its sorted order."""
        self.sorted_list.append(elt)
        j = len(self.sorted_list) - 1
        while j > 0 and self.sorted_list[j] < self.sorted_list[j - 1]:
            self.sorted_list[j], self.sorted_list[j - 1] = self.sorted_list[j - 1], self.sorted_list[j]
            j -= 1

    def insert(self, elt):
        if self.size() < self.k:
            self.insert_into_sorted_list(elt)
        else:
            self.insert_into_sorted_list(elt)
            displaced_element = self.sorted_list.pop()  # Pop the last element (k-th)
            self.heap.insert(displaced_element)

    def delete_from_top_k(self, j):
        """Delete the j-th element from the sorted list (A) and refill from the heap."""
        if 0 <= j < self.k:
            print("Index out of bounds.")
        if self.size() > self.k:
            print("Size must be greater than k.")

        self.sorted_list.pop(j)
        if self.heap.size() > 0:
            self.sorted_list.append(self.heap.min_element())
            self.heap.delete_min()


def run_tests():
    top_k_heap = TopKHeap(5)

    top_k_heap.sorted_list = [-10, -9, -8, -4, 0]
    [top_k_heap.heap.insert(elt) for elt in [1, 4, 5, 6, 15, 22, 31, 7]]

    print('Initial data structure:')
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)

    print('Test 1: Inserting element -2')
    top_k_heap.insert(-2)
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)
    assert top_k_heap.sorted_list == [-10, -9, -8, -4, -2]
    assert top_k_heap.heap.min_element() == 0
    top_k_heap.validate_data_structure()

    print('Test 2: Inserting element -11')
    top_k_heap.insert(-11)
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)
    assert top_k_heap.sorted_list == [-11, -10, -9, -8, -4]
    assert top_k_heap.heap.min_element() == -2
    top_k_heap.validate_data_structure()

    print('Test 3: Deleting element at index 3')
    top_k_heap.delete_from_top_k(3)
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)
    assert top_k_heap.sorted_list == [-11, -10, -9, -4, -2]
    assert top_k_heap.heap.min_element() == 0
    top_k_heap.validate_data_structure()

    print('Test 4: Deleting element at index 4')
    top_k_heap.delete_from_top_k(4)
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)
    assert top_k_heap.sorted_list == [-11, -10, -9, -4, 0]
    top_k_heap.validate_data_structure()

    print('Test 5: Deleting element at index 0')
    top_k_heap.delete_from_top_k(0)
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)
    assert top_k_heap.sorted_list == [-10, -9, -4, 0, 1]
    top_k_heap.validate_data_structure()

    print('Test 6: Deleting element at index 1')
    top_k_heap.delete_from_top_k(1)
    print('\t A = ', top_k_heap.sorted_list)
    print('\t H = ', top_k_heap.heap)
    assert top_k_heap.sorted_list == [-10, -4, 0, 1, 4]
    top_k_heap.validate_data_structure()

    print('Heap Top: All tests passed!')


if __name__ == "__main__":
    run_tests()
