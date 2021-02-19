from math import exp

from auxiliary.economics.factors import fgp


def subperiod_to_effective(r, n):
    return fgp(r, n) - 1


def nominal_to_effective(r, n):
    return subperiod_to_effective(r / n, n)


def continuous_to_effective(r):
    return exp(r) - 1


def simple_interest(r, t):
    return (1 + r) * t


def effective_interest(r, t):
    return fgp(r, t)


def subperiod_interest(r, n, t):
    return effective_interest(subperiod_to_effective(r, n), t)


def nominal_interest(r, n, t):
    return effective_interest(nominal_to_effective(r, n), t)


def continuous_interest(r, t):
    return effective_interest(continuous_to_effective(r), t)
