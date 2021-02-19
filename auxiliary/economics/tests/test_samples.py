from math import log
from unittest import main

from auxiliary.economics import effective_interest, nominal_interest, subperiod_interest, continuous_interest
from auxiliary.utils import ExtendedTestCase


class SampleTestCase(ExtendedTestCase):
    r, n, t = 0.1, 4, 2.5

    def test_factors(self):
        pass  # TODO: add tests

    def test_ints(self):
        factors = [
            effective_interest((1 + self.r / self.n) ** self.n - 1, self.t),
            subperiod_interest(self.r / self.n, self.n, self.t),
            nominal_interest(self.r, self.n, self.t),
            continuous_interest(log((1 + self.r / self.n) ** self.n), self.t),
        ]

        for factor in factors:
            self.assertAlmostEqual(factor, 1.2800845441963565)


if __name__ == '__main__':
    main()
