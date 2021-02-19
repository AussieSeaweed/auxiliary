def trim(values, percentage):
    n = int(len(values) * percentage)

    return values[n:len(values) - n]
