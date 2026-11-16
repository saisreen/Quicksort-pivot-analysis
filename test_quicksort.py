"""Run: python -m unittest -v"""
import random
import unittest
from quicksort import deterministic_quicksort, randomized_quicksort


class QuicksortTests(unittest.TestCase):
    def test_edge_cases(self):
        cases = [[], [7], [2, 1], [1, 1, 1, 1], [-5, 0, -2, 8],
                 [3, -1, 3, 0, -1], list(range(100)), list(range(99, -1, -1))]
        for case in cases:
            for algorithm in (deterministic_quicksort, randomized_quicksort):
                with self.subTest(case=case[:5], algorithm=algorithm.__name__):
                    actual = case.copy()
                    result = algorithm(actual)
                    self.assertIs(result, actual)
                    self.assertEqual(actual, sorted(case))

    def test_seeded_random_inputs(self):
        generator = random.Random(2026)
        for size in (0, 1, 10, 100, 500):
            for _ in range(12):
                case = [generator.randint(-20, 20) for _ in range(size)]
                for algorithm in (deterministic_quicksort, randomized_quicksort):
                    actual = case.copy()
                    algorithm(actual)
                    self.assertEqual(actual, sorted(case))


if __name__ == '__main__':
    unittest.main()
