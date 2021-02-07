import unittest
from math import log

from auxiliary.economics import ef_int, nom_int, sub_int, cont_int
from auxiliary.utils.tests.test_floats import FloatTestCase


class SampleTestCase(FloatTestCase):
    r, n, t = 0.1, 4, 2.5

    def test_factors(self):
        pass  # TODO: add tests

    def test_ints(self):
        factors = [
            ef_int((1 + self.r / self.n) ** self.n - 1, self.t),
            sub_int(self.r / self.n, self.n, self.t),
            nom_int(self.r, self.n, self.t),
            cont_int(log((1 + self.r / self.n) ** self.n), self.t),
        ]

        for factor in factors:
            self.assertAlmostEqual(factor, 1.2800845441963565)


if __name__ == '__main__':
    unittest.main()
