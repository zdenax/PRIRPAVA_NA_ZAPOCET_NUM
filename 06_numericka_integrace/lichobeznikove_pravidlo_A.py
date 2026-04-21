

def trapezoid_rule(f, a, b, n):
    """
    Numerické integrování (odhad určitého integrálu) pomocí lichoběžníkového pravidla.

    :param f: Integrovaná funkce f(x)
    :param a: Dolní mez integrace
    :param b: Horní mez integrace
    :param n: Počet podintervalů (lichoběžníků)
    :return: Odhad integrálu na [a, b] nebo None při chybě
    """
    import math
    if f is None or a is None or b is None or n is None:
        print("Error: Nil values are not supported.")
        return None
    if n <= 0:
        print("Error: n must be a positive integer.")
        return None
    if a == b:
        return 0.0
    if a > b:
        print("Error: a must be less than b.")
        return None
    h = (b - a) / n
    fa = f(a)
    fb = f(b)
    if math.isnan(fa) or math.isinf(fa) or math.isnan(fb) or math.isinf(fb):
        print("Error: Function returned NaN or Inf.")
        return None
    sum_val = 0.5 * (fa + fb)
    for i in range(1, n):
        x_i = a + i * h
        fxi = f(x_i)
        if math.isnan(fxi) or math.isinf(fxi):
            print("Error: Function returned NaN or Inf.")
            return None
        sum_val += fxi
    result = sum_val * h
    if math.isnan(result) or math.isinf(result):
        print("Error: Integration failed (result is NaN/Inf).")
        return None
    return result