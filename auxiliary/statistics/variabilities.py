from auxiliary.statistics.averages import mean


def rng(values):
    return max(values) - min(values)


def var(values):
    mean_value = mean(values)

    return sum((value - mean_value) ** 2 for value in values) / (len(values) - 1)


def std_dev(values):
    return var(values) ** 0.5
