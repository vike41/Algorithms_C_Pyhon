# median Heap algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing


from heap_min import MinHeap
from heap_max import MaxHeap


class MedianMaintainingHeap:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def satisfies_assertions(self):
        """Ensure the heap properties are maintained."""
        if self.min_heap.size() == 0:
            assert self.max_heap.size() == 0, "MinHeap is empty, MaxHeap should be empty."
            return
        if self.max_heap.size() == 0:
            assert self.min_heap.size() == 1, "MaxHeap is empty, MinHeap should have one element."
            return
        assert self.max_heap.max_element() <= self.min_heap.min_element(), (
            f'Max element of max heap = {self.max_heap.max_element()} is greater than '
            f'min element of min heap = {self.min_heap.min_element()}'
        )
        min_size = self.min_heap.size()
        max_size = self.max_heap.size()
        assert min_size == max_size or max_size == min_size - 1, (
            f'Heap sizes are unbalanced: MinHeap size = {min_size}, MaxHeap size = {max_size}'
        )

    def __repr__(self):
        return f'MaxHeap: {self.max_heap} MinHeap: {self.min_heap}'

    def get_median(self):
        """Retrieve the current median of the data."""
        if self.min_heap.size() == 0:
            assert self.max_heap.size() == 0, 'Heaps are unbalanced'
            raise ValueError('Cannot retrieve median from empty heaps')
        if self.max_heap.size() == 0:
            assert self.min_heap.size() == 1, 'Heaps are unbalanced'
            return self.min_heap.min_element()

        if self.max_heap.size() == self.min_heap.size():
            return (self.max_heap.max_element() + self.min_heap.min_element()) / 2
        return self.min_heap.min_element()

    def balance_heap_sizes(self):
        """Balance the sizes of the heaps."""
        while self.max_heap.size() + 1 < self.min_heap.size():
            self.max_heap.insert(self.min_heap.min_element())
            self.min_heap.delete_min()

        while self.max_heap.size() > self.min_heap.size():
            self.min_heap.insert(self.max_heap.max_element())
            self.max_heap.delete_max()

    def insert(self, value):
        """Insert a new value into the data structure."""
        if self.min_heap.size() == 0:
            self.min_heap.insert(value)
            return
        if self.max_heap.size() == 0:
            assert self.min_heap.size() == 1
            if value > self.min_heap.min_element():
                self.max_heap.insert(self.min_heap.min_element())
                self.min_heap.delete_min()
                self.min_heap.insert(value)
            else:
                self.max_heap.insert(value)
            return

        self.min_heap.insert(value)
        self.balance_heap_sizes()

    def delete_median(self):
        """Delete the current median."""
        self.max_heap.delete_max()
        self.balance_heap_sizes()


class TestMedianMaintainingHeap:
    def run_tests(self):
        m = MedianMaintainingHeap()
        print('Inserting values: 1, 5, 2, 4, 18, -4, 7, 9')

        test_cases = [
            (1, 1),
            (5, 3),
            (2, 2),
            (4, 3),
            (18, 4),
            (-4, 3),
            (7, 4),
            (9, 4.5)
        ]

        for value, expected_median in test_cases:
            m.insert(value)
            print(m)
            assert m.get_median() == expected_median, (
                f'Expected median = {expected_median}, got {m.get_median()}'
            )
            m.satisfies_assertions()

        print('All tests passed.')


if __name__ == "__main__":
    tester = TestMedianMaintainingHeap()
    tester.run_tests()
