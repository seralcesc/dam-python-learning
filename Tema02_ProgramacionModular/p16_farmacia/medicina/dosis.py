import fractions


def sumar_fraccion_dosis(f1_n, f1_d, f2_n, f2_d):
    frac1 = fractions.Fraction(f1_n, f1_d)
    frac2 = fractions.Fraction(f2_n, f2_d)
    return frac1 + frac2
