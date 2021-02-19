from math import sqrt

from auxiliary.statistics.averages import mean


def range(values):
    return max(values) - min(values)


def variance(values):
    mean_value = mean(values)

    return sum((value - mean_value) ** 2 for value in values) / (len(values) - 1)


def standard_deviation(values):
    return sqrt(variance(values))
