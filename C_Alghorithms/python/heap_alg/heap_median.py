# Heap Median algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing

from heap_min import MinHeap
from heap_max import MaxHeap


class MedianMaintainingHeap:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def __repr__(self):
        return f'MaxHeap: {self.max_heap} MinHeap: {self.min_heap}'

    def validate_heaps(self):
        """Check heap properties: MaxHeap should be less or equal to MinHeap."""
        if self.min_heap.size() == 0:
            assert self.max_heap.size() == 0, "Both heaps should be empty."
        if self.max_heap.size() == 0:
            assert self.min_heap.size() == 1, "MinHeap should contain only one element."
        if self.max_heap.size() > 0:
            assert self.max_heap.max_element() <= self.min_heap.min_element(), \
                f"MaxHeap element {self.max_heap.max_element()} exceeds MinHeap {self.min_heap.min_element()}."
        self.validate_heap_sizes()

    def validate_heap_sizes(self):
        """Ensure the size of MaxHeap is equal or one less than MinHeap."""
        min_size = self.min_heap.size()
        max_size = self.max_heap.size()
        assert min_size == max_size or min_size == max_size + 1, \
            f"Heap sizes are unbalanced. MinHeap: {min_size}, MaxHeap: {max_size}"

    def get_median(self):
        """Get the current median value from the heaps."""
        if self.min_heap.size() == 0:
            raise ValueError("Cannot retrieve median from empty heaps.")
        if self.max_heap.size() == 0:
            return self.min_heap.min_element()

        if self.min_heap.size() == self.max_heap.size():
            return (self.max_heap.max_element() + self.min_heap.min_element()) / 2
        return self.min_heap.min_element()

    def insert(self, value):
        """Insert a new element and balance the heaps."""
        if self.min_heap.size() == 0:
            self.min_heap.insert(value)
            return

        if self.max_heap.size() == 0:
            self.insert_into_proper_heap(value)
        else:
            self.min_heap.insert(value)
            self.balance_heaps()

    def insert_into_proper_heap(self, value):
        """Insert into the correct heap based on the value."""
        if value > self.min_heap.min_element():
            current_min = self.min_heap.min_element()
            self.min_heap.delete_min()
            self.min_heap.insert(value)
            self.max_heap.insert(current_min)
        else:
            self.max_heap.insert(value)

    def delete_median(self):
        """Delete the median element and balance the heaps."""
        self.max_heap.delete_max()
        self.balance_heaps()

    def balance_heaps(self):
        """Ensure that the heaps are balanced after insertions or deletions."""
        min_size = self.min_heap.size()
        max_size = self.max_heap.size()

        if max_size + 1 == min_size or max_size == min_size:
            return
        elif max_size > min_size:
            self.min_heap.insert(self.max_heap.max_element())
            self.max_heap.delete_max()
        else:
            self.max_heap.insert(self.min_heap.min_element())
            self.min_heap.delete_min()

        self.balance_heaps()


def test_median_maintaining_heap():
    median_heap = MedianMaintainingHeap()

    values = [1, 5, 2, 4, 18, -4, 7, 9]
    expected_medians = [1, 3, 2, 3, 4, 3, 4, 4.5]

    for i, value in enumerate(values):
        print(f"Inserting {value}")
        median_heap.insert(value)
        print(median_heap)
        median = median_heap.get_median()
        median_heap.validate_heaps()
        expected_median = expected_medians[i]
        assert median == expected_median, \
            f"Expected median {expected_median}, but got {median}"

    print("Median Heap: All tests passed!")


if __name__ == "__main__":
    test_median_maintaining_heap()
