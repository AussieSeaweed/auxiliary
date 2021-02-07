from auxiliary.utils import trim


def mean(values):
    return sum(values) / len(values)


def tr_mean(values, percentage):
    return mean(trim(sorted(values), percentage))


def median(values):
    values = sorted(values)

    if len(values) % 2:
        return values[len(values) // 2]
    else:
        return (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2
