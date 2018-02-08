import unittest

from src import compute


class ComputeTest(unittest.TestCase):

    def test_unordered_array(self):
        array = [1, 3, 6, 4, 1, 2]

        solution = compute.solution(array)
        print solution
        assert solution == 5

    def test_ordered_array(self):
        array = [1, 2, 3]

        solution = compute.solution(array)
        print solution
        assert solution == 4

    def test_array_with_negative_values(self):
        array = [-1, -3]

        solution = compute.solution(array)
        print solution
        assert solution == 1

    def test_with_single_entry_array(self):
        array = [5]

        solution = compute.solution(array)
        assert solution == 1

        array = [1]

        solution = compute.solution(array)
        assert solution == 2

    def test_with_positive_and_negative_values(self):
        array = [-2, -5, 4, 7, 533, 2000, -343, 1, 2, 3]

        solution = compute.solution(array)
        assert solution == 5

    def test_with_long_ordered_array(self):
        solution = compute.solution(range(100000))
        assert solution == 100000
