# Merge sort algorithm
# Based on Coursera Algorithms for searching, sorting and Indexing


class CrossoverFinder(object):
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.check_input(x, y)

    @staticmethod
    def check_input(x, y):
        if not len(x) == len(y):
            print("x and y must have the same length")
        if not x[0] > y[0]:
            print("x[0] must be greater than y[0]")
        if not x[-1] < y[-1]:
            print("x[-1] must be less than y[-1]")

    def find_crossover_index(self):
        return self._find_crossover_index_helper(0, len(self.x) - 1)

    def _find_crossover_index_helper(self, left, right):
        mid = (left + right) // 2

        if self.x[mid] > self.y[mid] and self.x[mid + 1] < self.y[mid + 1]:
            return mid
        elif self.x[mid] > self.y[mid]:
            return self._find_crossover_index_helper(mid + 1, right)
        else:
            return self._find_crossover_index_helper(left, mid)


class TestCrossoverFinder(object):

    @staticmethod
    def run_tests():
        test_cases = [
            ([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9], 1),
            ([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9], [1, 5]),
            ([0, 1], [-10, 10], 0),
            ([0, 1, 2, 3], [-10, -9, -8, 5], 2),
        ]

        for idx, (x, y, expected) in enumerate(test_cases, start=1):
            finder = CrossoverFinder(x, y)
            result = finder.find_crossover_index()
            if isinstance(expected, list):
                assert result in expected, f"Test Case #{idx} Failed"
            else:
                assert result == expected, f"Test Case #{idx} Failed"

        print('Merge Sort: All test cases passed')


if __name__ == "__main__":
    TestCrossoverFinder.run_tests()
