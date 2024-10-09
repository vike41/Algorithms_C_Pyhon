#include <iostream>
#include <vector>
#include <cassert>

class MinHeap {
    public:
        MinHeap() {
            heap.push_back(-1);  // Unused index 0 to simplify parent/child indexing
        }

        int size() const {
            return heap.size() - 1;
        }

        void print() const {
            for (size_t i = 1; i < heap.size(); ++i) {
                std::cout << heap[i] << " ";
            }
            std::cout << std::endl;
        }

        void satisfies_assertions() const {
            for (size_t i = 2; i < heap.size(); ++i) {
                int parent = i / 2;
                assert(heap[i] >= heap[parent] && "Min-heap property fails");
            }
        }

        int min_element() const {
            if (size() < 1) {
                throw std::out_of_range("Heap is empty");
            }
            return heap[1];
        }

        void insert(int value) {
            heap.push_back(value);
            bubble_up(size());
        }

        void delete_min() {
            if (size() > 1) {
                heap[1] = heap.back();
                heap.pop_back();
                bubble_down(1);
            }
            else if (size() == 1) {
                heap.pop_back(); 
            }
        }

    private:
        std::vector<int> heap;  // Heap stored as a vector (1-based index)

        // Restore heap order by moving an element upwards
        void bubble_up(int index) {
            while (index > 1) {
                int parent_index = index / 2;
                if (heap[parent_index] <= heap[index]) break;
                swap(index, parent_index);
                index = parent_index;
            }
        }

        // Restore heap order by moving an element downwards
        void bubble_down(int index) {
            while (2 * index <= size()) {
                int left_child = 2 * index;
                int right_child = 2 * index + 1;
                int smallest_child = left_child;

                if (right_child <= size() && heap[right_child] < heap[left_child]) {
                    smallest_child = right_child;
                }

                if (heap[index] <= heap[smallest_child]) break;

                swap(index, smallest_child);
                index = smallest_child;
            }
        }

        void swap(int i, int j) {
            int temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
};

class TestMinHeap {
public:
    static void run_tests() {
        MinHeap h;

        std::cout << "Inserting: 5, 2, 4, -1, 7 in that order." << std::endl;
        h.insert(5);
        h.print();
        assert(h.min_element() == 5);

        h.insert(2);
        h.print();
        assert(h.min_element() == 2);

        h.insert(4);
        h.print();
        assert(h.min_element() == 2);

        h.insert(-1);
        h.print();
        assert(h.min_element() == -1);

        h.insert(7);
        h.print();
        assert(h.min_element() == -1);

        h.satisfies_assertions();

        std::cout << "Deleting minimum element:" << std::endl;
        h.delete_min();
        h.print();
        assert(h.min_element() == 2);

        h.delete_min();
        h.print();
        assert(h.min_element() == 4);

        h.delete_min();
        h.print();
        assert(h.min_element() == 5);

        h.delete_min();
        h.print();
        assert(h.min_element() == 7);

        h.delete_min();
        h.print();
        assert(h.size() == 0);

        std::cout << "Heap Min: All tests passed!" << std::endl;
    }
};
