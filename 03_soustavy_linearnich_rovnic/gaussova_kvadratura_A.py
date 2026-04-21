
def gauss_quadrature(f, a, b, n):
    """
    Numerická integrace pomocí Gaussovy kvadratury (pro 2 nebo 3 uzly).

    :param f: Integrovaná funkce f(x)
    :param a: Dolní mez integrace
    :param b: Horní mez integrace
    :param n: Počet uzlů (2 nebo 3)
    :return: Odhad integrálu na [a, b] nebo None při chybě
    """
    import math
    if f is None or a is None or b is None or n is None:
        print("Error: Nil values are not supported.")
        return None
    if a == b:
        return 0.0
    if a > b:
        print("Error: a must be less than b.")
        return None
    if n == 2:
        nodes = [-math.sqrt(1/3), math.sqrt(1/3)]
        weights = [1.0, 1.0]
    elif n == 3:
        nodes = [-math.sqrt(3/5), 0.0, math.sqrt(3/5)]
        weights = [5/9, 8/9, 5/9]
    else:
        print("Error: Unsupported number of nodes (use 2 or 3).")
        return None
    m = 0.5 * (a + b)
    half_len = 0.5 * (b - a)
    result = 0.0
    for i in range(len(nodes)):
        xi = m + half_len * nodes[i]
        fxi = f(xi)
        if math.isnan(fxi) or math.isinf(fxi):
            print("Error: Function returned NaN or Inf.")
            return None
        result += weights[i] * fxi
    result *= half_len
    if math.isnan(result) or math.isinf(result):
        print("Error: Integration failed (result is NaN/Inf).")
        return None
    return result