# Max Heap algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing


class MaxHeap:
    def __init__(self):
        """Initialize an empty MaxHeap with a placeholder None at index 0."""
        self.heap = [None]

    def size(self):
        """Return the number of elements in the MaxHeap."""
        return len(self.heap) - 1

    def __repr__(self):
        """Return a string representation of the heap."""
        return str(self.heap[1:])

    def satisfies_assertions(self):
        """Check if the MaxHeap satisfies the heap property."""
        for i in range(2, len(self.heap)):
            assert self.heap[i] <= self.heap[i // 2], (
                f'Maxheap property fails at position {i // 2}, parent elt: {self.heap[i // 2]}, child elt: {self.heap[i]}'
            )

    def max_element(self):
        """Return the maximum element (root) of the MaxHeap."""
        assert self.size() > 0, "Cannot get max element from an empty heap"
        return self.heap[1]

    def bubble_up(self, index):
        """Bubble up an element to restore heap order."""
        while index > 1:
            parent_index = index // 2
            if self.heap[parent_index] >= self.heap[index]:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def bubble_down(self, index):
        """Bubble down an element to restore heap order."""
        while 2 * index <= self.size():
            lchild_index = 2 * index
            rchild_index = 2 * index + 1
            max_child_index = lchild_index

            if rchild_index <= self.size() and self.heap[rchild_index] > self.heap[lchild_index]:
                max_child_index = rchild_index

            if self.heap[index] >= self.heap[max_child_index]:
                break

            self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
            index = max_child_index

    def insert(self, element):
        """Insert a new element into the MaxHeap."""
        self.heap.append(element)
        self.bubble_up(self.size())

    def delete_max(self):
        """Delete the maximum element (root) from the MaxHeap."""
        assert self.size() > 0, "Cannot delete max element from an empty heap"
        if self.size() == 1:
            self.heap.pop()
        else:
            self.heap[1] = self.heap.pop()
            self.bubble_down(1)


class TestMaxHeap:
    def run_tests(self):
        max_heap = MaxHeap()
        print('Inserting: 5, 2, 4, -1, and 7 in that order.')

        elements = [5, 2, 4, -1, 7]
        expected_max = [5, 5, 5, 5, 7]

        for i, elt in enumerate(elements):
            max_heap.insert(elt)
            print(f'\t Heap after inserting {elt} = {max_heap}')
            assert max_heap.max_element() == expected_max[i], f"Test failed: expected max = {expected_max[i]}"

        max_heap.satisfies_assertions()

        # Deletion tests
        print('Deleting maximum element')
        expected_max_after_deletions = [5, 4, 2, -1, None]

        for expected in expected_max_after_deletions:
            max_heap.delete_max()
            print(f'\t Heap = {max_heap}')
            if max_heap.size() > 0:
                assert max_heap.max_element() == expected, f"Test failed: expected max = {expected}"

        print('All tests passed.')


if __name__ == "__main__":
    tester = TestMaxHeap()
    tester.run_tests()
