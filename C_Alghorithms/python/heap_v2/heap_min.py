# Min Heap algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing

class MinHeap:
    def __init__(self):
        """Initialize an empty MinHeap with a placeholder None at index 0."""
        self.heap = [None]

    def size(self):
        """Return the number of elements in the MinHeap."""
        return len(self.heap) - 1

    def __repr__(self):
        """Return a string representation of the MinHeap."""
        return str(self.heap[1:])

    def satisfies_assertions(self):
        """Check if the MinHeap satisfies the heap property."""
        for i in range(2, len(self.heap)):
            assert self.heap[i] >= self.heap[i // 2], (
                f'Min heap property fails at position {i // 2}, parent elt: {self.heap[i // 2]}, child elt: {self.heap[i]}'
            )

    def min_element(self):
        """Return the minimum element (root) of the MinHeap."""
        assert self.size() > 0, "Cannot get min element from an empty heap"
        return self.heap[1]

    def bubble_up(self, index):
        """Bubble up an element to restore heap order."""
        while index > 1:
            parent_index = index // 2
            if self.heap[parent_index] <= self.heap[index]:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def bubble_down(self, index):
        """Bubble down an element to restore heap order."""
        while 2 * index <= self.size():
            lchild_index = 2 * index
            rchild_index = 2 * index + 1
            min_child_index = lchild_index

            if rchild_index <= self.size() and self.heap[rchild_index] < self.heap[lchild_index]:
                min_child_index = rchild_index

            if self.heap[index] <= self.heap[min_child_index]:
                break

            self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
            index = min_child_index

    def insert(self, element):
        """Insert a new element into the MinHeap."""
        self.heap.append(element)
        self.bubble_up(self.size())

    def delete_min(self):
        """Delete the minimum element (root) from the MinHeap."""
        assert self.size() > 0, "Cannot delete min element from an empty heap"
        if self.size() == 1:
            self.heap.pop()
        else:
            self.heap[1] = self.heap.pop()
            self.bubble_down(1)


class TestMinHeap:
    def run_tests(self):
        min_heap = MinHeap()
        print('Inserting: 5, 2, 4, -1, and 7 in that order.')

        elements = [5, 2, 4, -1, 7]
        expected_min = [5, 2, 2, -1, -1]

        for i, elt in enumerate(elements):
            min_heap.insert(elt)
            print(f'\t Heap after inserting {elt} = {min_heap}')
            assert min_heap.min_element() == expected_min[i], f"Test failed: expected min = {expected_min[i]}"

        min_heap.satisfies_assertions()

        # Deletion tests
        print('Deleting minimum element')
        expected_min_after_deletions = [2, 4, 5, 7, None]

        for expected in expected_min_after_deletions:
            min_heap.delete_min()
            print(f'\t Heap = {min_heap}')
            if min_heap.size() > 0:
                assert min_heap.min_element() == expected, f"Test failed: expected min = {expected}"

        print('All tests passed.')


if __name__ == "__main__":
    tester = TestMinHeap()
    tester.run_tests()
