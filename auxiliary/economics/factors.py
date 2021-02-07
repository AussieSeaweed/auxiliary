def fgp(i, n):
    return (1 + i) ** n


def pgf(i, n):
    return 1 / fgp(i, n)


def fga(i, n):
    return 1 / agf(i, n)


def agf(i, n):
    return agp(i, n) * pgf(i, n)


def pga(i, n):
    return ((1 + i) ** n - 1) / (i * (1 + i) ** n)


def agp(i, n):
    return 1 / pga(i, n)


def pgg(i, n):
    return (1 - (1 + i * n) / (1 + i) ** n) / i ** 2


def pggeom(i, g, n):
    return pga((1 + i) / (1 + g) - 1, n) / (1 + g)


def pgperp(i):
    return 1 / i
