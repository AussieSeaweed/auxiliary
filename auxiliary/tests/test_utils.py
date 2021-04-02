from typing import Optional, cast
from unittest import main

from auxiliary import ExtendedTestCase, bind, default, get, next_or_none


class UtilsTestCase(ExtendedTestCase):
    def test_next_or_none(self) -> None:
        self.assertEqual(next_or_none(iter(range(3))), 0)
        self.assertEqual(next_or_none(iter(())), None)

    def test_get(self) -> None:
        self.assertEqual(get(300), 300)
        self.assertRaises(TypeError, get, None)

    def test_default(self) -> None:
        self.assertEqual(default(300, 100), 300)
        self.assertEqual(default(cast(Optional[int], None), 100), 100)

    def test_bind(self) -> None:
        self.assertEqual(bind(1, 0, 2), 1)
        self.assertEqual(bind(-100, 0, 2), 0)
        self.assertEqual(bind(100, 0, 2), 2)
        self.assertRaises(ValueError, bind, 100, 2, 0)


if __name__ == '__main__':
    main()
