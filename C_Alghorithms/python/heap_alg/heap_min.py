# Min Heap algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing


class MinHeap:
    def __init__(self):
        self.heap = [None]

    def size(self) -> int:
        return len(self.heap) - 1

    def __repr__(self) -> str:
        return str(self.heap[1:])

    def satisfies_assertions(self) -> None:
        """Ensures that the heap satisfies the min-heap property."""
        for i in range(2, len(self.heap)):
            parent = i // 2
            assert self.heap[i] >= self.heap[parent], \
                f'Min-heap property fails at index {parent}, parent: {self.heap[parent]}, child: {self.heap[i]}'

    def min_element(self) -> int:
        return self.heap[1]

    def bubble_up(self, index: int) -> None:
        """Bubbles up the element at the given index to restore heap order."""
        while index > 1:
            parent_index = index // 2
            if self.heap[parent_index] <= self.heap[index]:
                break
            self._swap(index, parent_index)
            index = parent_index

    def bubble_down(self, index: int) -> None:
        """Bubbles down the element at the given index to restore heap order."""
        while 2 * index < len(self.heap):
            left_child = 2 * index
            right_child = 2 * index + 1

            smallest_child = left_child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
                smallest_child = right_child

            if self.heap[index] <= self.heap[smallest_child]:
                break

            self._swap(index, smallest_child)
            index = smallest_child

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.bubble_up(self.size())

    def delete_min(self) -> None:
        """Deletes the minimum element (the root) from the heap."""
        if self.size() > 1:
            self.heap[1] = self.heap.pop()
            self.bubble_down(1)
        elif self.size() == 1:
            self.heap.pop()  # Remove last element if only one remains

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class TestMinHeap:

    @staticmethod
    def run_tests() -> None:
        h = MinHeap()

        print('Inserting: 5, 2, 4, -1, 7 in that order.')
        h.insert(5)
        print(f'\tHeap = {h}')
        assert h.min_element() == 5

        h.insert(2)
        print(f'\tHeap = {h}')
        assert h.min_element() == 2

        h.insert(4)
        print(f'\tHeap = {h}')
        assert h.min_element() == 2

        h.insert(-1)
        print(f'\tHeap = {h}')
        assert h.min_element() == -1

        h.insert(7)
        print(f'\tHeap = {h}')
        assert h.min_element() == -1

        h.satisfies_assertions()

        print('Deleting minimum element:')
        h.delete_min()
        print(f'\tHeap = {h}')
        assert h.min_element() == 2

        h.delete_min()
        print(f'\tHeap = {h}')
        assert h.min_element() == 4

        h.delete_min()
        print(f'\tHeap = {h}')
        assert h.min_element() == 5

        h.delete_min()
        print(f'\tHeap = {h}')
        assert h.min_element() == 7

        h.delete_min()
        print(f'\tHeap = {h}')
        assert h.size() == 0

        print('Heap Min: All tests passed!')


if __name__ == "__main__":
    TestMinHeap.run_tests()

