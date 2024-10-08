# Min Heap algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing

class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def size(self) -> int:
        return len(self.heap) - 1

    def __repr__(self) -> str:
        return str(self.heap[1:])

    def satisfies_assertions(self) -> None:
        for i in range(2, len(self.heap)):
            parent_index = i // 2
            assert self.heap[i] <= self.heap[parent_index], \
                f'Max-heap property fails at index {parent_index}, parent: {self.heap[parent_index]}, child: {self.heap[i]}'

    def max_element(self) -> int:
        """Returns the maximum element, which is the root of the heap."""
        return self.heap[1]

    def bubble_up(self, index: int) -> None:
        """Bubbles up the element at the given index to restore heap order."""
        while index > 1:
            parent_index = index // 2
            if self.heap[parent_index] >= self.heap[index]:
                break
            self._swap(index, parent_index)
            index = parent_index

    def bubble_down(self, index: int) -> None:
        """Bubbles down the element at the given index to restore heap order."""
        while 2 * index <= self.size():
            left_child = 2 * index
            right_child = 2 * index + 1
            largest_child = left_child

            if right_child <= self.size() and self.heap[right_child] > self.heap[left_child]:
                largest_child = right_child

            if self.heap[index] >= self.heap[largest_child]:
                break

            self._swap(index, largest_child)
            index = largest_child

    def insert(self, value: int) -> None:
        """Inserts a new element into the heap."""
        self.heap.append(value)
        self.bubble_up(self.size())

    def delete_max(self) -> None:
        """Deletes the maximum element (the root) from the heap."""
        if self.size() > 1:
            self.heap[1] = self.heap.pop()
            self.bubble_down(1)
        elif self.size() == 1:
            self.heap.pop()

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class TestMaxHeap:
    @staticmethod
    def run_tests() -> None:
        h = MaxHeap()

        print('Inserting: 5, 2, 4, -1, 7 in that order.')
        h.insert(5)
        print(f'\tHeap = {h}')
        assert h.max_element() == 5

        h.insert(2)
        print(f'\tHeap = {h}')
        assert h.max_element() == 5

        h.insert(4)
        print(f'\tHeap = {h}')
        assert h.max_element() == 5

        h.insert(-1)
        print(f'\tHeap = {h}')
        assert h.max_element() == 5

        h.insert(7)
        print(f'\tHeap = {h}')
        assert h.max_element() == 7

        h.satisfies_assertions()

        print('Deleting maximum element')
        h.delete_max()
        print(f'\tHeap = {h}')
        assert h.max_element() == 5

        h.delete_max()
        print(f'\tHeap = {h}')
        assert h.max_element() == 4

        h.delete_max()
        print(f'\tHeap = {h}')
        assert h.max_element() == 2

        h.delete_max()
        print(f'\tHeap = {h}')
        assert h.max_element() == -1

        # Test delete_max on heap of size 1, should result in empty heap.
        h.delete_max()
        print(f'\tHeap = {h}')
        assert h.size() == 0

        print('All tests passed!')



TestMaxHeap.run_tests()
