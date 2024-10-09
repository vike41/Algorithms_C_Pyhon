#include <iostream>
#include <vector>
#include <stdexcept>
#include <cassert>


class MaxHeap {

    public:
        MaxHeap() {
            heap.push_back(-1); 
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
                int parent_index = i / 2;
                assert(heap[i] <= heap[parent_index] && "Max-heap property fails");
            }
        }

        // Return the maximum element (the root of the heap)
        int max_element() const {
            if (size() < 1) {
                throw std::out_of_range("Heap is empty");
            }
            return heap[1];
        }

        void insert(int value) {
            heap.push_back(value);
            bubble_up(size());
        }

        // Delete the maximum element (the root of the heap)
        void delete_max() {
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
        std::vector<int> heap;  // The heap, stored as a 1-based index array

        // Bubble up the element at the given index to restore heap order
        void bubble_up(int index) {
            while (index > 1) {
                int parent_index = index / 2;
                if (heap[parent_index] >= heap[index]) break;
                swap(index, parent_index);
                index = parent_index;
            }
        }

        // Bubble down the element at the given index to restore heap order
        void bubble_down(int index) {
            while (2 * index <= size()) {
                int left_child = 2 * index;
                int right_child = 2 * index + 1;
                int largest_child = left_child;

                if (right_child <= size() && heap[right_child] > heap[left_child]) {
                    largest_child = right_child;
                }

                if (heap[index] >= heap[largest_child]) break;

                swap(index, largest_child);
                index = largest_child;
            }
        }

        // Swap two elements in the heap
        void swap(int i, int j) {
            int temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
};


class TestMaxHeap {
    public:
        static void run_tests() {
            MaxHeap h;

            std::cout << "Inserting: 5, 2, 4, -1, 7 in that order." << std::endl;
            h.insert(5);
            h.print();
            assert(h.max_element() == 5);

            h.insert(2);
            h.print();
            assert(h.max_element() == 5);

            h.insert(4);
            h.print();
            assert(h.max_element() == 5);

            h.insert(-1);
            h.print();
            assert(h.max_element() == 5);

            h.insert(7);
            h.print();
            assert(h.max_element() == 7);

            h.satisfies_assertions();

            std::cout << "Deleting maximum element" << std::endl;
            h.delete_max();
            h.print();
            assert(h.max_element() == 5);

            h.delete_max();
            h.print();
            assert(h.max_element() == 4);

            h.delete_max();
            h.print();
            assert(h.max_element() == 2);

            h.delete_max();
            h.print();
            assert(h.max_element() == -1);

            // Test delete_max on heap of size 1, should result in empty heap.
            h.delete_max();
            h.print();
            assert(h.size() == 0);

            std::cout << "Heap Max: All tests passed!" << std::endl;
        }
};
