from itertools import chain
from unittest import main

from auxiliary import (ExtendedTestCase, after, chunked, const, flattened, iter_equal, product, rotated, sum_, trimmed,
                       unique, windowed)


class IterablesTestCase(ExtendedTestCase):
    def test_windowed(self) -> None:
        self.assert2DIterableEqual(windowed(iter(range(6)), 3), (range(3), range(1, 4), range(2, 5), range(3, 6)))
        self.assert2DIterableEqual(windowed(range(6), 6), (range(6),))
        self.assert2DIterableEqual(windowed(range(6), 7), ())
        self.assert2DIterableEqual(windowed(range(6), 0), ((), (), (), (), (), (), ()))
        self.assert2DIterableEqual(windowed(iter(range(6)), 3, partial=True), (
            range(3), range(1, 4), range(2, 5), range(3, 6), range(4, 6), range(5, 6),
        ))

    def test_chunked(self) -> None:
        self.assert2DIterableEqual(chunked(iter(range(7)), 3), (range(3), range(3, 6), range(6, 7)))
        self.assert2DIterableEqual(chunked(range(5), 2), (range(2), range(2, 4), range(4, 5)))
        self.assert2DIterableEqual(chunked(range(5), 1), (range(1), range(1, 2), range(2, 3), range(3, 4), range(4, 5)))
        self.assert2DIterableEqual(chunked(range(5), 1), (range(1), range(1, 2), range(2, 3), range(3, 4), range(4, 5)))

    def test_flattened(self) -> None:
        self.assertIterableEqual(flattened((range(5), range(5, 10))), range(10))

    def test_trimmed(self) -> None:
        self.assertIterableEqual(trimmed(iter(range(10)), 0), range(10))
        self.assertIterableEqual(trimmed(range(10), 0.1), range(1, 9))
        self.assertIterableEqual(trimmed(range(5), 0.1), range(5))
        self.assertIterableEqual(trimmed(range(10), 0.5), ())
        self.assertIterableEqual(trimmed(iter((1, 2, 3)), 1 / 3), (2,))

    def test_rotated(self) -> None:
        self.assertIterableEqual(rotated(iter(range(6)), -1), chain((5,), range(5)))
        self.assertIterableEqual(rotated(range(6), 0), range(6))
        self.assertIterableEqual(rotated(range(6), 2), chain(range(2, 6), range(2)))

    def test_after(self) -> None:
        self.assertEqual(after(iter(range(6)), 0), 1)
        self.assertEqual(after(range(6), 4), 5)
        self.assertEqual(after(range(0, 6, 2), 2), 4)
        self.assertEqual(after(range(6), 5, True), 0)
        self.assertRaises(ValueError, after, range(6), 5)
        self.assertRaises(ValueError, after, range(6), -1)

    def test_iter_equal(self) -> None:
        self.assertTrue(iter_equal(iter(range(6)), iter(range(6))))
        self.assertTrue(iter_equal(iter(range(6)), range(6)))
        self.assertTrue(iter_equal([0, 1, 2], iter((0, 1, 2))))
        self.assertTrue(iter_equal((), []))
        self.assertFalse(iter_equal(range(7), range(6)))
        self.assertFalse(iter_equal(range(1, 7), range(6)))
        self.assertFalse(iter_equal((), (0,)))

    def test_const(self) -> None:
        self.assertTrue(const(iter((1, 1, 1))))
        self.assertTrue(const(()))
        self.assertTrue(const(((1, 1), (1, 1))))
        self.assertFalse(const(range(10)))
        self.assertFalse(const(iter(range(10))))

    def test_unique(self) -> None:
        self.assertFalse(unique(iter((1, 1, 1))))
        self.assertTrue(unique(()))
        self.assertFalse(unique(((1, 1), (1, 1), (1, 2))))
        self.assertFalse(unique(([2, 1], [1, 1], [2, 1])))
        self.assertTrue(unique(([2, 1], [1, 1], [1, 2])))
        self.assertTrue(unique(range(10)))
        self.assertTrue(unique(iter(range(10))))

    def test_sum(self) -> None:
        self.assertEqual(sum_(iter(range(6))), 15)
        self.assertEqual(sum_(range(1, 6)), 15)
        self.assertEqual(sum_(range(1, 6), 1), 16)
        self.assertEqual(sum_((), 1), 1)
        self.assertRaises(ValueError, sum_, ())

    def test_product(self) -> None:
        self.assertEqual(product(iter(range(6))), 0)
        self.assertEqual(product(range(1, 6)), 120)
        self.assertEqual(product(range(1, 6), 1), 120)
        self.assertEqual(product((), 1), 1)
        self.assertRaises(ValueError, product, ())


if __name__ == '__main__':
    main()
