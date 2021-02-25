from itertools import chain, zip_longest
from unittest import main

from auxiliary.tests.utils import ExtendedTestCase
from auxiliary.utils import constant, iter_equal, limit, product, rotate, sum_, trim, window


class UtilsTestCase(ExtendedTestCase):
    def test_trim(self) -> None:
        self.assertIterableEqual(trim(range(10), 0), range(10))
        self.assertIterableEqual(trim(range(10), 0.1), range(1, 9))
        self.assertIterableEqual(trim(range(5), 0.1), range(5))
        self.assertIterableEqual(trim(range(10), 0.5), ())
        self.assertIterableEqual(trim(iter([1, 2, 3]), 1 / 3), [2])

    def test_window(self) -> None:
        for x, y in zip(window(range(6), 3), [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]):
            self.assertSequenceEqual(x, y)
        for x, y in zip(window(range(6), 6), [[0, 1, 2, 3, 4, 5]]):
            self.assertSequenceEqual(x, y)
        for x, y in zip(window(iter(range(6)), 7), [[0, 1, 2, 3, 4, 5]]):
            self.assertSequenceEqual(x, y)
        for x, y in zip_longest(window([1, 2, 3, 4, 5, 6], 0), [[], [], [], [], [], [], []], fillvalue=None):
            self.assertSequenceEqual(x, y)

    def test_rotate(self) -> None:
        self.assertIterableEqual(rotate(range(6), -1), [5, 0, 1, 2, 3, 4])
        self.assertIterableEqual(rotate(range(6), 0), range(6))
        self.assertIterableEqual(rotate(iter(range(6)), 2), chain(range(2, 6), range(2)))

    def test_iter_equal(self) -> None:
        self.assertTrue(iter_equal(range(6), iter(range(6))))
        self.assertTrue(iter_equal([0, 1, 2], (0, 1, 2)))
        self.assertTrue(iter_equal([], []))
        self.assertFalse(iter_equal([], [0]))

    def test_sum(self) -> None:
        self.assertEqual(sum_(range(6)), 15)
        self.assertRaises(ValueError, sum_, ())

    def test_product(self) -> None:
        self.assertEqual(product(range(6)), 0)
        self.assertEqual(product(range(1, 6)), 120)
        self.assertRaises(ValueError, product, ())

    def test_limit(self) -> None:
        self.assertEqual(limit(1, 0, 2), 1)
        self.assertEqual(limit(-100, 0, 2), 0)
        self.assertEqual(limit(100, 0, 2), 2)
        self.assertRaises(ValueError, limit, 100, 2, 0)

    def test_constant(self) -> None:
        self.assertTrue(constant([1, 1, 1]))
        self.assertTrue(constant(()))
        self.assertFalse(constant(iter(range(10))))


if __name__ == '__main__':
    main()
