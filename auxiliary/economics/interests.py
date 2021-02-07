from math import exp

from auxiliary.economics.factors import fgp


def sub_to_ef(r, n):
    return fgp(r, n) - 1


def nom_to_ef(r, n):
    return sub_to_ef(r / n, n)


def cont_to_ef(r, exp=exp):
    return exp(r) - 1


def simple_int(r, t):
    return (1 + r) * t


def ef_int(r, t):
    return fgp(r, t)


def sub_int(r, n, t):
    return ef_int(sub_to_ef(r, n), t)


def nom_int(r, n, t):
    return ef_int(nom_to_ef(r, n), t)


def cont_int(r, t):
    return ef_int(cont_to_ef(r), t)
