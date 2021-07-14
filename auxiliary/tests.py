from itertools import chain, repeat
from unittest import TestCase, main

from auxiliary import bind, chunk, const, distinct, flatten, next_or_none, prod, reverse_args, rotate, window


class AuxiliaryTestCase(TestCase):
    def test_window(self):
        self.assertSequenceEqual(
            tuple(window(iter(range(6)), 3)),
            tuple(map(tuple, (range(3), range(1, 4), range(2, 5), range(3, 6)))),
        )
        self.assertSequenceEqual(tuple(window(range(6), 6)), (range(6),))
        self.assertSequenceEqual(tuple(window(range(6), 7)), ())
        self.assertSequenceEqual(tuple(window(tuple(range(6)), 0)), ((), (), (), (), (), (), ()))
        self.assertSequenceEqual(tuple(window(iter(range(6)), 3, partial=True)), tuple(map(tuple, (
            range(3), range(1, 4), range(2, 5), range(3, 6), range(4, 6), range(5, 6),
        ))))

    def test_chunk(self):
        self.assertSequenceEqual(
            tuple(chunk(iter(range(7)), 3)),
            tuple(map(tuple, (range(3), range(3, 6), range(6, 7)))),
        )
        self.assertSequenceEqual(tuple(chunk(range(5), 2)), (range(2), range(2, 4), range(4, 5)))
        self.assertSequenceEqual(
            tuple(chunk(range(5), 1)),
            (range(1), range(1, 2), range(2, 3), range(3, 4), range(4, 5)),
        )
        self.assertSequenceEqual(
            tuple(chunk(list(range(5)), 1)),
            tuple(map(list, (range(1), range(1, 2), range(2, 3), range(3, 4), range(4, 5)))),
        )

    def test_flatten(self):
        self.assertSequenceEqual(tuple(flatten((range(5), range(5, 10)))), range(10))

    def test_rotate(self):
        self.assertSequenceEqual(rotate(iter(range(6)), -1), tuple(chain((5,), range(5))))
        self.assertSequenceEqual(rotate(range(6), 0), range(6))
        self.assertSequenceEqual(rotate(range(6), 2), tuple(chain(range(2, 6), range(2))))

    def test_distinct(self):
        self.assertFalse(distinct(iter((1, 1, 1))))
        self.assertTrue(distinct(()))
        self.assertFalse(distinct(((1, 1), (1, 1), (1, 2))))
        self.assertFalse(distinct(([2, 1], [1, 1], [2, 1])))
        self.assertTrue(distinct(([2, 1], [1, 1], [1, 2])))
        self.assertTrue(distinct(range(10)))
        self.assertTrue(distinct(iter(range(10))))

    def test_const(self):
        self.assertTrue(const(iter((1, 1, 1))))
        self.assertTrue(const(()))
        self.assertTrue(const(((1, 1), (1, 1))))
        self.assertFalse(const(range(10)))
        self.assertFalse(const(iter(range(10))))

    def test_prod(self):
        self.assertEqual(prod(iter(range(1, 10))), 362880)
        self.assertEqual(prod(repeat(1, 5)), 1)
        self.assertEqual(prod(()), 1)

    def test_bind(self):
        self.assertEqual(bind(1, 0, 2), 1)
        self.assertEqual(bind(-100, 0, 2), 0)
        self.assertEqual(bind(100, 0, 2), 2)
        self.assertRaises(ValueError, bind, 100, 2, 0)

    def test_next_or_none(self):
        self.assertEqual(next_or_none(iter(range(3))), 0)
        self.assertIsNone(next_or_none(iter(())))

    def test_reverse_args(self):
        self.assertEqual(reverse_args(range)(5, 1), range(1, 5))
        self.assertEqual(reverse_args(dict)(foo='foo', bar='bar'), {'foo': 'foo', 'bar': 'bar'})
        x, y = [], []
        self.assertIs(max(x, y), x)
        self.assertIs(reverse_args(max)(x, y), y)


if __name__ == '__main__':
    main()
