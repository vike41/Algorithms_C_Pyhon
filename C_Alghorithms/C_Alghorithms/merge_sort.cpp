#include <iostream>
#include <vector>
#include <cassert>
#include <tuple>
#include <algorithm>


class CrossoverFinder 
{
    public:
        CrossoverFinder(const std::vector<int>& x, const std::vector<int>& y)
            : x(x), y(y) {
            check_input(x, y);
        }

        int find_crossover_index() {
            return find_crossover_index_helper(0, x.size() - 1);
        }

    private:

        std::vector<int> x;
        std::vector<int> y;

        void check_input(const std::vector<int>& x, const std::vector<int>& y) {
            if (x.size() != y.size()) {
                std::cerr << "x and y must have the same length" << std::endl;
                exit(EXIT_FAILURE);
            }
            if (x[0] <= y[0]) {
                std::cerr << "x[0] must be greater than y[0]" << std::endl;
                exit(EXIT_FAILURE);
            }
            if (x.back() >= y.back()) {
                std::cerr << "x[-1] must be less than y[-1]" << std::endl;
                exit(EXIT_FAILURE);
            }
        }

    int find_crossover_index_helper(int left, int right) {
        int mid = (left + right) / 2;

        if (x[mid] > y[mid] && x[mid + 1] < y[mid + 1]) {
            return mid;
        }
        else if (x[mid] > y[mid]) {
            return find_crossover_index_helper(mid + 1, right);
        }
        else {
            return find_crossover_index_helper(left, mid);
        }
    }
};


class TestCrossoverFinder 
{
    public:
        static void run_tests() {

            std::vector<std::tuple<std::vector<int>, std::vector<int>, std::vector<int>>> test_cases = {
                std::make_tuple(std::vector<int>{0, 1, 2, 3, 4, 5, 6, 7}, std::vector<int>{-2, 0, 4, 5, 6, 7, 8, 9}, std::vector<int>{1}),
                std::make_tuple(std::vector<int>{0, 1, 2, 3, 4, 5, 6, 7}, std::vector<int>{-2, 0, 4, 4, 4, 4, 8, 9}, std::vector<int>{1, 5}),
                std::make_tuple(std::vector<int>{0, 1}, std::vector<int>{-10, 10}, std::vector<int>{0}),
                std::make_tuple(std::vector<int>{0, 1, 2, 3}, std::vector<int>{-10, -9, -8, 5}, std::vector<int>{2})
            };

            for (size_t i = 0; i < test_cases.size(); ++i) {

                const std::vector<int>& x = std::get<0>(test_cases[i]);
                const std::vector<int>& y = std::get<1>(test_cases[i]);
                const std::vector<int>& expected = std::get<2>(test_cases[i]);

                CrossoverFinder finder(x, y);
                int result = finder.find_crossover_index();

                // Check if result is in the list of expected results
                if (std::find(expected.begin(), expected.end(), result) == expected.end()) {
                    std::cerr << "Test Case #" << i + 1 << " Failed: Expected one of {";
                    for (int val : expected) std::cerr << val << " ";
                    std::cerr << "} but got " << result << std::endl;
                    exit(EXIT_FAILURE);
                }
            }

            std::cout << "Mege Sort: All test cases passed." << std::endl;
        }
    };

